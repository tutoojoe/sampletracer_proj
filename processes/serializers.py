from rest_framework import serializers
from .models import Processes


class ProcessesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processes
        fields = "__all__"
