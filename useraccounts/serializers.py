from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from django.conf import settings

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from dj_rest_auth.registration.serializers import RegisterSerializer

# the dj-rest-auth is providing user serializer already. So we can use it for development.
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class UserSerializer(serializers.Serializer):
#     class Meta:
#         model = User
#         fields = ['first_name','last_name','username','email']
