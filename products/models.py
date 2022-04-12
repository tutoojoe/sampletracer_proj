from django.db import models

# Create your models here.


class Season(models.Model):
    season = models.CharField(max_length=10)

    def __str__(self):
        return self.season


class ProductGroup(models.Model):
    product_group = models.CharField(max_length=20)

    def __str__(self):
        return self.product_group


class Style(models.Model):
    style_no = models.CharField(
        max_length=20, unique=True, blank=False, null=False)
    style_description = models.TextField(max_length=100)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    product_group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.style_no}'
