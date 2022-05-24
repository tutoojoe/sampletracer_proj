from rest_framework import serializers

from products.models import (MeasurementChart, Measurements, Season,
                             ProductGroup, Processes, Accessories, Style,
                             Colors, StyleCombo)


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
        model = Processes
        fields = "__all__"


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


class MeasurementItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = "__all__"


class MeasurementSerializer(serializers.ModelSerializer):
    measurements = MeasurementItemSerializer(
        source='measurements_set', many=True, read_only=True)

    class Meta:
        model = MeasurementChart
        fields = "__all__"


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = "__all__"


class StyleComboSerializer(serializers.ModelSerializer):
    class Meta:
        model = StyleCombo
        fields = "__all__"
