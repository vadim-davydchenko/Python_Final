from rest_framework import serializers
from .models import Server

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ('id', 'server_ip', 'server_name', 'server_is_active')

class ServerStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ('server_ip', 'server_is_active')