from django.db import models

from common.models import Common


class Website(Common):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    dev = models.BooleanField(default=True)
    freq = models.IntegerField(default=0)
    category = models.ForeignKey(
        "property.Category", on_delete=models.CASCADE, related_name="websites"
    )
    stage = models.ForeignKey(
        "property.Stage", on_delete=models.CASCADE, related_name="websites"
    )

    def __str__(self):
        if self.dev:
            return f'{self.category} {self.name} 개발 {self.stage}'
        return f'{self.category} {self.name} 운영 {self.stage}'

    class Meta:
        ordering = ["order"]
