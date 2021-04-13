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


class WebSite(Common):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    dev = models.BooleanField(default=True)
    freq = models.IntegerField(default=0)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="websites"
    )
    stage = models.ForeignKey(
        "Stage", on_delete=models.CASCADE, related_name="websites"
    )
    websites = models.Manager()  # manager 설정

    def __str__(self):
        if self.dev:
            return f'{self.category} {self.name} 개발 {self.stage}'
        return f'{self.category} {self.name} 운영 {self.stage}'

    class Meta:
        ordering = ["order"]
