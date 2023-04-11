Collecting and sending data about the system to the server, which we did in the previous lesson. This is a free task in which you need to show imagination. However, the program must provide the following features:

When starting the program, it should register our client on the server ( POST request to api/servers/add)
To determine the external IP address, use requests.get('https://ifconfig.me/ip').text, or use any other available method to determine the IP.
In the name field, enter the hostname value
In the description field, take the value from the environment variable
The program must process the system data received from the psutil utility and send it to the server at 1-minute intervals
The program logs the following stages of work:
- INFO Program start,
- INFO Successful server registration,
- INFO An array of data about the system obtained as a result of the work,
- ERROR When sending data or registering the server failed.
