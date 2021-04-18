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

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name

