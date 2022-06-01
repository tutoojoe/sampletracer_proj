from rest_framework import serializers
from .models import Accessories


class AccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = "__all__"
