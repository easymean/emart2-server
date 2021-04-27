from django.db import models

from common.models import Common


class Category(Common):
  name = models.CharField(max_length=50)
  description = models.TextField(default='')

  def __str__(self):
    return f'{self.name}'

  class Meta:
    ordering = ["order"]

  def save(self, *args, **kwargs):
    ins = Category.objects.filter(*args, **kwargs).count()
    if ins == 0:
      self.order = Category.objects.filter(is_active=True).count() + 1
    super().save(*args, **kwargs)


class Stage(Common):
  name = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.name}'

  class Meta:
    ordering = ["order"]

  def save(self, *args, **kwargs):
    ins = Stage.objects.filter(*args, **kwargs).count()
    if ins == 0:
      self.order = Stage.objects.filter(is_active=True).count() + 1
    super().save(*args, **kwargs)
