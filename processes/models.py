from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from products.models import Style
from suppliers.models import Suppliers


# Create your models here.
User = get_user_model()


class Processes(models.Model):
    style_no = models.ForeignKey(
        Style, related_name="processes", on_delete=models.CASCADE)
    process_name = models.CharField(_("Accessories name"), max_length=50)
    purchase_units = models.CharField(_("Purchase units"), max_length=10)
    qty_per_item = models.DecimalField(
        _("Quantity per item"), max_digits=10, decimal_places=3)

    supplier = models.ForeignKey(
        Suppliers, on_delete=models.SET_NULL, blank=True, null=True)
    task_status = models.BooleanField(default=False, blank=True, null=True)

    assigned_to = models.ManyToManyField(
        User, related_name=_("process_assigned_to"), blank=True, null=True)
    assigned_by = models.ManyToManyField(User)
    target_date = models.DateField(blank=True, null=True)
    finish_date = models.DateField(blank=True, null=True)

    @property
    def status(self):
        if self.task_status:
            return "Completed"
        return "Not Completed"

    @property
    def process_qty(self):
        return (self.style_no.quantity * self.qty_per_item)

    def __str__(self):

        return f'Style No - {self.style_no}| Process - {self.process_name}| Processing Status - {self.status}'

    class Meta:
        ordering = ["-id"]
        verbose_name = "Process"
        verbose_name_plural = "Processes"
