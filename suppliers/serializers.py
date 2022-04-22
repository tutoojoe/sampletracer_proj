from rest_framework import serializers
from django.conf import settings
from suppliers.models import Suppliers


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        exclude = ['created_at', 'last_update_at']
