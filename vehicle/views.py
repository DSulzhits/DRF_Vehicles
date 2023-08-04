from rest_framework import viewsets, generics

from vehicle.models import Car, Motorcycle, Mileage
from vehicle.serializers import CarSerializer, MotorcycleSerializer, MileageSerializer, MotorcycleMileageSerializer, \
    CarCreateSerializer


class CarCreateAPIView(generics.CreateAPIView):
    serializer_class = CarCreateSerializer


class CarRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarListAPIView(generics.ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarUpdateAPIView(generics.UpdateAPIView):  # поддерживает как PUT так и PATCH
    serializer_class = CarSerializer


class CarDestroyAPIView(generics.DestroyAPIView):
    queryset = Car.objects.all()


class MotorcycleViewSet(viewsets.ModelViewSet):
    serializer_class = MotorcycleSerializer
    queryset = Motorcycle.objects.all()


class MileageCreateAPIView(generics.CreateAPIView):
    serializer_class = MileageSerializer


class MileageMotorcycleAPIView(generics.ListAPIView):
    queryset = Mileage.objects.filter(motorcycle__isnull=False)
    serializer_class = MotorcycleMileageSerializer
