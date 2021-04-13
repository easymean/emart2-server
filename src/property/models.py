from django.db import models

from common.models import Common


class Category(Common):
  name = models.CharField(max_length=50)
  description = models.TextField(default='')

  def __str__(self):
    return f'{self.name}'

  class Meta:
    ordering = ["order"]


class Stage(Common):
  name = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.name}'

  class Meta:
    ordering = ["order"]
