from rest_framework import serializers
from .models import MeasurementChart, Measurements


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
