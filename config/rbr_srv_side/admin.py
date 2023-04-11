from django.contrib import admin
from .models import Server
# Register your models here.


class ServerAdmin(admin.ModelAdmin):
    list_display = ('id', 'server_ip', 'server_name', 'server_is_active')

admin.site.register(Server, ServerAdmin)