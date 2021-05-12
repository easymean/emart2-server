from django.db import models

from common.hasher import encrypt
from common.models import Common


class AccountManager(models.Manager):
    def create_account(self, **kwargs):
        kwargs['server_id'] = encrypt(kwargs['server_id'])
        kwargs['server_password'] = encrypt(kwargs['server_password'])
        return self.create(**kwargs)


class Account(Common):
    server_name = models.CharField(max_length=50)
    server_ip = models.CharField(max_length=50)
    server_id = models.CharField(max_length=100)
    server_password = models.CharField(max_length=100)

    objects = AccountManager()

    def __str__(self):
        return f'{self.server_name}'

    def save(self, *args, **kwargs):
        account = Account.objects.create_account(**kwargs)
        super().save(account)
