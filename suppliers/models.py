import email
from django.db import models

# Create your models here.


class Suppliers(models.Model):
    supplier_name = models.CharField(max_length=50,)
    contact_person = models.CharField(max_length=50)
    supplier_email = models.EmailField(max_length=200)
    supplier_phone = models.CharField(max_length=15)
    supplier_address = models.TextField(max_length=255)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.supplier_name
