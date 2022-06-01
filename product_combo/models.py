from django.db import models
from django.utils.translation import gettext_lazy as _
from products.models import Style
from product_colors.models import Colors

# Create your models here.


class StyleCombo(models.Model):
    style_no = models.ForeignKey(
        Style, on_delete=models.CASCADE, null=True, blank=True)
    color = models.ManyToManyField(Colors)
    quantity = models.PositiveIntegerField(
        _("Quantity required"), default=0)

    def __str__(self):
        return f'{self.color} - {self.quantity} nos'
