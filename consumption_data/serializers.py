from rest_framework import serializers

from .models import Energy_consumption


class EnergyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Energy_consumption
        fields = '__all__'
