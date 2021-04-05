from django.db import models

from src.common.models import Common


class WebSite(Common):
  name = models.CharField(max_length=100)
  url = models.URLField(max_length=100)
  dev = models.BooleanField(default=True)
  freq = models.IntegerField(default=0)
  category = models.ForeignKey(
    "category.Category", on_delete=models.CASCADE, related_name="websites"
  )
  websites = models.Manager()  # manager 설정

  def __str__(self):
    return f'{self.name}'

  class Meta:
    ordering = ["order"]
