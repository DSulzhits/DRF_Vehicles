from rest_framework import viewsets, generics

from vehicle.models import Car, Motorcycle
from vehicle.serializers import CarSerializer, MotorcycleSerializer


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class MotorcycleCreateAPIView(generics.CreateAPIView):
    serializer_class = MotorcycleSerializer


class MotorcycleListAPIView(generics.ListAPIView):
    serializer_class = MotorcycleSerializer
    queryset = Motorcycle.objects.all()


class MotorcycleRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MotorcycleSerializer
    queryset = Motorcycle.objects.all()


class MotorcycleUpdateAPIView(generics.UpdateAPIView):  # поддерживает как PUT так и PATCH
    serializer_class = MotorcycleSerializer
    queryset = Motorcycle.objects.all()


class MotorcycleDestroyAPIView(generics.DestroyAPIView):
    queryset = Motorcycle.objects.all()
