# from useraccounts.models import User
from urllib import response
from useraccounts.serializers import CustomerSerializer
from useraccounts.models import Customer
from useraccounts.serializers import UserTypeUpdateSerializer
# from useraccounts.models import User
from useraccounts.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.http import Http404

# Create your views here.
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework import status
from rest_framework_simplejwt.views import token_verify
from rest_framework.views import APIView
from useraccounts.permissions import MerchUserPermission, NewUserPermission, StoreKeeperPermission


# if you want to use Authorization Code Grant, use this
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://127.0.0.1:8000/api/user/google/callback/"
    client_class = OAuth2Client

# class GoogleLogin(SocialLoginView): # if you want to use Implicit Grant, use this
#     adapter_class = GoogleOAuth2Adapter


User = get_user_model()


class UsersListAPIView(generics.ListAPIView):
    """
    Lists out all the uses in the project. View is limited to admin user only.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUser]


class UserTypeDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserTypeUpdateSerializer
    # permission_classes = [IsAdminUser]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserTypeUpdateSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserTypeUpdateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserDetailsSerializer
    # permission_classes = [IsAuthenticated]

    token_verify

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserDetailsSerializer(user)
        return Response(serializer.data)


class CustomerListAPIView(generics.ListCreateAPIView):
    """_Views the list of customers or/and can add customer_

    Args:
        generics (_type_): _description_
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """_Customer - Retrieve, Update , Delete details of Customer_

    Args:
        generics (_pk_): _primary key_

    Returns:
        _object_: _object details_
    """
    serializer_class = CustomerSerializer
    permission_classes = []

    def get_queryset(self):
        return Customer.objects.all()


class DashboardAPIView(APIView):
    permission_classes = [MerchUserPermission]

    def get(self, request, format=None):

        return Response({"message": "New user requested dashboard"})

    def get(self, request, format=None):
        permission_classes = [MerchUserPermission]
        return Response({"message": "Merch requested dashboard"})

    def get(self, request, format=None):
        permission_classes = [StoreKeeperPermission]
        return Response({"message": "New user requested dashboard"})
