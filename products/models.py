from ast import Assign
from email.policy import default
from telnetlib import STATUS
from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime

from pytz import timezone
from useraccounts.models import Customer

from suppliers.models import Suppliers
from useraccounts.models import Merchandiser

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
        max_length=50, unique=True, blank=False, null=False)
    style_description = models.TextField(
        _("Style description"), max_length=100)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    product_group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    quantity = models.IntegerField(_("Quantity required"), default=0)
    delivery_date = models.DateField(
        _("Delivery date"), default=datetime.date.today)
    merchandiser = models.ForeignKey(Merchandiser, verbose_name=_(
        "Merchandiser name"), related_name="merchandiser", on_delete=models.CASCADE)
    customer = models.ForeignKey(
        Customer, verbose_name=_("Customer name"), related_name="customer", on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(
        auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.style_no} | Delivery date: {self.delivery_date}'

    class Meta:
        ordering = ["-created_on"]
        verbose_name = "Style"
        verbose_name_plural = "Styles"


class Accessories(models.Model):
    style_no = models.ForeignKey(
        Style, related_name="accessories", on_delete=models.CASCADE)  # this 'related_name' field helps in nesting and listing data.
    item_name = models.CharField(_("Accessories name"), max_length=50)
    purchase_units = models.CharField(_("Purchase units"), max_length=10)
    qty_per_item = models.DecimalField(
        _("Quantity per item"), max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(
        Suppliers, on_delete=models.SET_NULL, blank=True, null=True)

    task_status = models.BooleanField(default=False)

    @property
    def status(self):
        if self.task_status:
            return "Completed"
        return "Not Completed"

    def __str__(self):
        # return 'Style No: %s item: %s, Quantity: %f,Supplier: %s' % (self.style_no, self.item_name, self.qty_per_item, self.supplier)
        return 'Style No: %s item: %s | Status: %s' % (self.style_no, self.item_name, self.status)

    class Meta:
        ordering = ["item_name"]
        verbose_name = "Accessory"
        verbose_name_plural = "Accessories"


class Processes(models.Model):
    style_no = models.ForeignKey(
        Style, related_name="processes", on_delete=models.CASCADE)
    process_name = models.CharField(_("Accessories name"), max_length=50)
    purchase_units = models.CharField(_("Purchase units"), max_length=10)
    qty_per_item = models.DecimalField(
        _("Quantity per item"), max_digits=10, decimal_places=2)

    supplier = models.ForeignKey(
        Suppliers, on_delete=models.SET_NULL, blank=True, null=True)
    task_status = models.BooleanField(default=False)

    @property
    def status(self):
        if self.task_status:
            return "Completed"
        return "Not Completed"

    @property
    def process_qty(self):
        return (self.style_no.quantity * self.qty_per_item)

    def __str__(self):
        # return f'Process: {self.process_name}, Quantity:{ self.qty_per_item}, Process Quantity:{ self.process_qty},Supplier: {self.supplier}'
        return f'Style No - {self.style_no} | Process - {self.process_name} | Processing Status - { self.status}'

    class Meta:
        ordering = ["process_name"]
        verbose_name = "Process"
        verbose_name_plural = "Processes"


class MeasurementChart(models.Model):
    mc_name = models.CharField(_("Measurement Chart"), max_length=100)
    description = models.CharField(
        _("Short description"), max_length=200, default="measurement chart", help_text=_("eg: Mens Tshirt"))

    def __str__(self):
        return f'{self.mc_name} | {self.description}'


class Measurements(models.Model):
    mc_name = models.ForeignKey(MeasurementChart, on_delete=models.CASCADE)
    size = models.CharField(max_length=100)
    measuringpoint = models.CharField(max_length=200)
    tolerance = models.DecimalField(
        default=0.5, max_digits=5, decimal_places=2)
    measurement = models.DecimalField(
        default=0, max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.mc_name.mc_name} | {self.size}'
