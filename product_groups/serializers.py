from rest_framework import serializers
from .models import ProductGroup


class ProductGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGroup
        fields = "__all__"
