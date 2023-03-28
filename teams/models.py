from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Category:
    TEAMS_CATEGORY = (
        ("domestic", "Domestic"),
        ("international", "International"),
        ("national", "National"),
        ("league", "League"),
    )


class Teams(models.Model):
    logo = models.ImageField(upload_to="media/team-images/", default=None)
    code_name = models.CharField(max_length=10)
    name = models.CharField(max_length=256)
    category = models.CharField(
        choices=Category.TEAMS_CATEGORY,
        max_length=100,
    )
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=2,
        null=True,
    )
    champions = models.IntegerField(default=0)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name + "_" + self.code_name

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
