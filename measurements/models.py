from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class MeasurementChart(models.Model):
    mc_name = models.CharField(_("Measurement Chart"), max_length=100)
    description = models.CharField(
        _("Short description"), max_length=200, default="measurement chart",
        help_text=_("eg: Mens Tshirt"))

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
