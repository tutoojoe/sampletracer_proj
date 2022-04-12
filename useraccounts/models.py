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


class NewUserManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=User.UserTypes.NEWUSER)


class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=User.UserTypes.CUSTOMER)


class ManagerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=User.UserTypes.MANAGER)


class JuniorEmpManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=User.UserTypes.JUNIOREMP)


class StorekeeperManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=User.UserTypes.STOREKEEPER)


class NewUser(User):
    objects = NewUserManager()

    class Meta:
        proxy = True

    def usertype(self):
        return "NewUser"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = User.UserTypes.NEWUSER
        return super().save(*args, **kwargs)


class Manager(User):
    objects = ManagerManager()

    class Meta:
        proxy = True

    def usertype(self):
        return "Manager"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = User.UserTypes.MANAGER
        return super().save(*args, **kwargs)


class Customer(User):
    objects = CustomerManager()

    class Meta:
        proxy = True

    def usertype(self):
        return "Customer"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = User.UserTypes.CUSTOMER
        return super().save(*args, **kwargs)


class JuniorEmp(User):
    objects = JuniorEmpManager()

    class Meta:
        proxy = True

    def usertype(self):
        return "JuniorEmployee"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = User.UserTypes.JUNIOREMP
        return super().save(*args, **kwargs)


class Storekeeper(User):
    objects = StorekeeperManager()

    class Meta:
        proxy = True

    def usertype(self):
        return "Storekeeper"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = User.UserTypes.STOREKEEPER
        return super().save(*args, **kwargs)
