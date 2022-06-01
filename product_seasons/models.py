from django.db import models

# Create your models here.


class Season(models.Model):
    season = models.CharField(max_length=10)

    def __str__(self):
        return self.season
