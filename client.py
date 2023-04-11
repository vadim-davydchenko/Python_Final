import os
import socket
import requests
import json
import logging
import time
from requests.exceptions import RequestException
import psutil

logging.basicConfig(level=logging.INFO)

API_URL = "http://127.0.0.1:8000/api/servers/"
REGISTER_URL = API_URL + "add"
EXTERNAL_IP = requests.get("https://ifconfig.me/ip").text
HOSTNAME = socket.gethostname()
DESCRIPTION = os.getenv("SERVER_DESCRIPTION", "Default description")

def register_server():
    payload = {
        "server_ip": EXTERNAL_IP,
        "name": HOSTNAME,
        "description": DESCRIPTION,
        "server_is_active": True,
    }

    try:
        response = requests.post(REGISTER_URL, data=payload)
        response.raise_for_status()
        logging.info("Successful server registration")
        return response.json()
    except RequestException as e:
        logging.error(f"Error registering server: {e}")
        return None

def collect_system_data():
    host_information = {
        "sysname": os.uname().sysname,
        "hostname": HOSTNAME,
    }

    network = [
        {
            "interface": name,
            "up_down": "up" if addrs[2] else "down",
            "mtu": addrs[4],
        }
        for name, addrs in psutil.net_if_addrs().items()
    ]

    disk = [
        {
            "disk": partition.device,
            "mountpoint": partition.mountpoint,
            "file_system_type": partition.fstype,
            "total": disk_usage.total,
            "used": disk_usage.used,
        }
        for partition, disk_usage in zip(psutil.disk_partitions(), map(psutil.disk_usage, [p.mountpoint for p in psutil.disk_partitions()]))
    ]

    memory = psutil.virtual_memory()
    memory_data = {
        "memory_total": memory.total,
        "memory_used": memory.used,
        "memory_percent": memory.percent,
    }

    cpu = {
        "cpu_cores": psutil.cpu_count(),
        "cpu_physical_cores": psutil.cpu_count(logical=False),
        "cpu_frequency": psutil.cpu_freq()._asdict(),
    }

    load_average = dict(zip(["1 min", "5 min", "15 min"], os.getloadavg()))

    system_data = {
        "host_information": host_information,
        "network": network,
        "disk": disk,
        "memory": memory_data,
        "cpu": cpu,
        "load_average": load_average,
    }

    return system_data

def send_system_data(server_id):
    headers = {"Content-Type": "application/json"}
    url = f"{API_URL}{server_id}/"
    system_data = collect_system_data()

    try:
        response = requests.patch(url, data=json.dumps(system_data), headers=headers)
        response.raise_for_status()
        logging.info("System data sent successfully")
    except RequestException as e:
        logging.error(f"Error sending system data: {e}")

def main():
    logging.info("Program start")
    server = register_server()

    if server:
        while True:
            send_system_data(server["id"])
            time.sleep(60)

if __name__ == "__main__":
    main()
