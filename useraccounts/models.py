from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Create your models here.


class User(AbstractUser):

    class UserTypes(models.TextChoices):
        NEWUSER = "NEWUSER", "NewUser"
        MANAGER = "MANAGER", "Manager"
        CUSTOMER = "CUSTOMER", "Customer"
        JUNIOREMP = "JUNIOREMP", "JuniorEmp"
        STOREKEEPER = "STOREKEEPER", "Storekeeper"

    user_type = models.CharField(
        _("Type of user"), max_length=50, choices=UserTypes.choices, default=UserTypes.NEWUSER)
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.email


class NewUser(User):
    class Meta:
        proxy = True


class Manager(User):
    class Meta:
        proxy = True


class Customer(User):
    class Meta:
        proxy = True


class JuniorEmp(User):
    class Meta:
        proxy = True


class Storekeeper(User):
    class Meta:
        proxy = True
