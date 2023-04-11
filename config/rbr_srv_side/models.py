from django.db import models

# Create your models here.
class Server(models.Model):
    server_ip = models.GenericIPAddressField('IP', max_length=16, default='0.0.0.0')
    server_name= models.TextField('name', max_length=255, default='server')
    server_is_active = models.BooleanField(default=False)

    class Meta:
        managed = True
        verbose_name = 'Server'