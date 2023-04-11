from django.shortcuts import render
from rest_framework import viewsets
from .models import Server
from .serializers import ServerSerializer, ServerStatusSerializer
# Create your views here.


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ServerStatusViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerStatusSerializer
