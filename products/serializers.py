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


class AccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = "__all__"


class ProcessesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGroup
        fields = "__all__"


class StyleSerializer(serializers.ModelSerializer):
    # accessories = AccessoriesSerializer(many=True)
    # processes = ProcessesSerializer(many=True)

    class Meta:
        model = Style
        fields = ['style_no', 'style_description', 'season', 'product_group',
                  'size', 'quantity', 'delivery_date', 'accessories_set', 'processes_set']
