from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime

from suppliers.models import Suppliers

# Create your models here.


class Season(models.Model):
    season = models.CharField(max_length=10)

    def __str__(self):
        return self.season


class ProductGroup(models.Model):
    product_group = models.CharField(_("Product group"), max_length=20)

    def __str__(self):
        return self.product_group


class Style(models.Model):
    style_no = models.CharField(
        max_length=20, unique=True, blank=False, null=False)
    style_description = models.TextField(
        _("Style description"), max_length=100)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    product_group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    quantity = models.IntegerField(_("Quantity required"), default=0)
    delivery_date = models.DateField(
        _("Delivery date"), default=datetime.date.today)

    def __str__(self):
        return f'{self.style_no}'


class Accessories(models.Model):
    style_no = models.ForeignKey(Style, on_delete=models.CASCADE)
    item_name = models.CharField(_("Accessories name"), max_length=50)
    purchase_units = models.CharField(_("Purchase units"), max_length=10)
    qty_per_item = models.DecimalField(
        _("Quantity per item"), max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(
        Suppliers, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.item_name


class Processes(models.Model):
    style_no = models.ForeignKey(Style, on_delete=models.CASCADE)
    process_name = models.CharField(_("Accessories name"), max_length=50)
    purchase_units = models.CharField(_("Purchase units"), max_length=10)
    qty_per_item = models.DecimalField(
        _("Quantity per item"), max_digits=10, decimal_places=2)

    supplier = models.ForeignKey(
        Suppliers, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.process_name
