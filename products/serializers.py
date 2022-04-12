from rest_framework import serializers

from products.models import Season, ProductGroup, Processes, Accessories, Style


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = "__all__"


class ProductGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGroup
        fields = "__all__"


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = "__all__"


class AccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = "__all__"


class ProcessesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGroup
        fields = "__all__"
