from rest_framework import serializers

from vehicle.models import Car, Motorcycle


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class MotorcycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorcycle
        fields = '__all__'
