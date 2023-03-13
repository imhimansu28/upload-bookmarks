from django.db import models
from django.urls import reverse
from django.utils import timezone


class Bookmark(models.Model):
    title = models.CharField(max_length=255, blank=True)
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def _get_absolute_url(self):
        return reverse("bookmark:bookmark", args=(self.title))

    def __str__(self):
        return self.title
