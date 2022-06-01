from .models import StyleCombo
from rest_framework import serializers


class StyleComboSerializer(serializers.ModelSerializer):
    class Meta:
        model = StyleCombo
        fields = "__all__"
