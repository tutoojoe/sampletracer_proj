from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Create your models here.


class User(AbstractUser):

    class UserTypes(models.TextChoices):
        ADMINUSER = "ADMINUSER", "AdminUser"
        NEWUSER = "NEWUSER", "NewUser"
        MERCHANDISER = "MERCHANDISER", "Merchandiser"
        CUSTOMER = "CUSTOMER", "Customer"
        JUNIOREMP = "JUNIOREMP", "JuniorEmp"
        STOREKEEPER = "STOREKEEPER", "Storekeeper"

    user_type = models.CharField(
        _("Type of user"), max_length=50, help_text="User type/role - to be selected from the given list. This will determine the permissions. \nDefault value will be NEWUSER on registration.", choices=UserTypes.choices, default=UserTypes.NEWUSER)
    username = None
    email = models.EmailField(
        _('email address'), help_text="Email address of user for registration and login purposes", unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'


class NewUserManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=User.UserTypes.NEWUSER)


class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=User.UserTypes.CUSTOMER)


class MerchandiserManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=User.UserTypes.MERCHANDISER)


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


class Merchandiser(User):
    objects = MerchandiserManager()

    class Meta:
        proxy = True

    def usertype(self):
        return "Merchandiser"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = User.UserTypes.MERCHANDISER
        return super().save(*args, **kwargs)


class Customer(User):
    objects = CustomerManager()

    @property
    def more(self):
        return self.customermore

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


class CustomerMore(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address_line_1 = models.CharField(max_length=255)
    address_line_1 = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.customer.first_name} - {self.customer.email}'
