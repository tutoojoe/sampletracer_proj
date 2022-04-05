from rest_framework import serializers


# the dj-rest-auth is providing user serializer already. So we can use it for development.
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class UserSerializer(serializers.Serializer):
#     class Meta:
#         model = User
#         fields = ['first_name','last_name','username','email']