from django.db import models

from common.models import Common


class Account(Common):
    server_name = models.CharField(max_length=50)
    server_ip = models.CharField(max_length=50)
    server_id = models.CharField(max_length=100)
    server_password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.server_name}'

    def save(self, *args, **kwargs):
        return