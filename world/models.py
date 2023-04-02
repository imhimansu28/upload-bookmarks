from django.db import models
from django.utils import timezone


class Country(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    mobile_code = models.CharField(max_length=10, blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.name} - {self.code}"
