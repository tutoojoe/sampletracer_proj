
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from django.conf import settings

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from dj_rest_auth.registration.serializers import RegisterSerializer

# the dj-rest-auth is providing user serializer already.
# So we can use it for development.


# from useraccounts.models import User
from django.contrib.auth import get_user_model

from useraccounts.models import Customer, Merchandiser, CustomerMore, NewUser
# from useraccounts.views import User

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserTypeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'user_type']


class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerMore
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    customer_details = CustomerDetailSerializer(
        source='customermore_set', read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name',
                  'email', 'customer_details', 'is_active']


class MerchandiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchandiser
        fields = ['id', 'first_name', 'last_name', 'email', 'is_active']
