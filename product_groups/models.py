from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class ProductGroup(models.Model):
    product_group = models.CharField(_("Product group"), max_length=20)

    def __str__(self):
        return self.product_group
