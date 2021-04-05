from django.db import models


class Common(models.Model):
  is_active = models.BooleanField(default=True)
  created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)
  order = models.IntegerField(default=0)

  class Meta:
    abstract = True
