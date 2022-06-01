from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from useraccounts.models import User
from products.models import Style
from suppliers.models import Suppliers

# Create your models here.


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
    assigned_to = models.ManyToManyField(
        User, related_name=_("accessory_assigned_to"), blank=True, null=True)
    assigned_by = models.ManyToManyField(User)
    target_date = models.DateField(blank=True, null=True)
    finish_date = models.DateField(blank=True, null=True)

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
