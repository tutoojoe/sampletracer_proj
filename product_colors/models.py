from django.db import models

# Create your models here.


class Colors(models.Model):
    color_name = models.CharField(max_length=100)
    pantone_no = models.CharField(
        max_length=30, unique=True, null=True, blank=True)

    def __str__(self):
        return f'{self.color_name} {self.pantone_no}'

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'
