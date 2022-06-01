from rest_framework import serializers
from product_groups.models import ProductGroup
from product_seasons.models import Season

from products.models import Style


class StyleSerializer(serializers.ModelSerializer):
    accessories = serializers.StringRelatedField(many=True, read_only=True)
    processes = serializers.StringRelatedField(many=True, read_only=True)
    product_group = serializers.StringRelatedField()
    season = serializers.StringRelatedField()

    class Meta:
        model = Style
        fields = "__all__"
        depth = 0


class StyleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = "__all__"


class StyleDetailedSerializer(serializers.ModelSerializer):
    accessories = serializers.StringRelatedField(many=True, read_only=True)
    processes = serializers.StringRelatedField(many=True, read_only=True)
    # season = serializers.StringRelatedField()
    group = serializers.PrimaryKeyRelatedField(
        queryset=ProductGroup.objects.all(), source='product_group',
        write_only=True
    )
    season_pk = serializers.PrimaryKeyRelatedField(
        queryset=Season.objects.all(), source='season', write_only=True
    )
    # product_group = serializers.StringRelatedField()

    # accessories = AccessoriesSerializer(many=True)
    # processes = ProcessesSerializer(many=True)

    class Meta:
        model = Style
        # fields = "__all__"
        fields = ['style_no', 'style_description', 'season', 'season_pk',
                  'product_group', 'group', 'size', 'quantity',
                  'delivery_date', 'accessories', 'processes']
        # depth = 0
