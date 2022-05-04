from rest_framework.permissions import BasePermission
from useraccounts.models import Storekeeper, User, NewUser, Merchandiser, Customer


class NewUserPermission(BasePermission):
    def has_permission(self, request, view):
        print("inside permission check newuserpermission")
        is_user = NewUser.objects.filter(pk=request.user.pk).exists()
        print(is_user, " new user this is the status")
        return is_user


class MerchUserPermission(BasePermission):
    def has_permission(self, request, view):
        print("inside permission check merchandiserpermission")
        is_user = Merchandiser.objects.filter(pk=request.user.pk).exists()
        print(is_user, " merch this is the status")
        return is_user


class StoreKeeperPermission(BasePermission):
    def has_permission(self, request, view):
        print("inside permission check storekeeperpermission")
        is_user = Storekeeper.objects.filter(pk=request.user.pk).exists()
        print(is_user, " store - this is the status")
        return is_user
