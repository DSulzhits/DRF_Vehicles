from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny

from vehicle.models import Car, Motorcycle, Mileage
from vehicle.serializers import CarSerializer, MotorcycleSerializer, MileageSerializer, MotorcycleMileageSerializer, \
    CarCreateSerializer
from vehicle.permissions import IsOwnerOrStaff
from vehicle.paginators import VehiclePaginator


class CarCreateAPIView(generics.CreateAPIView):
    """Car create endpoint"""
    serializer_class = CarCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_car = serializer.save()
        new_car.owner = self.request.user
        new_car.save()


class CarRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarListAPIView(generics.ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarUpdateAPIView(generics.UpdateAPIView):  # поддерживает как PUT так и PATCH
    serializer_class = CarSerializer
    permission_classes = [IsOwnerOrStaff]


class CarDestroyAPIView(generics.DestroyAPIView):
    queryset = Car.objects.all()


class MotorcycleViewSet(viewsets.ModelViewSet):
    """ViewSet fot Motorcycles"""
    serializer_class = MotorcycleSerializer
    queryset = Motorcycle.objects.all()
    permission_classes = [AllowAny]
    pagination_class = VehiclePaginator


class MileageCreateAPIView(generics.CreateAPIView):
    serializer_class = MileageSerializer


class MileageMotorcycleAPIView(generics.ListAPIView):
    queryset = Mileage.objects.filter(motorcycle__isnull=False)
    serializer_class = MotorcycleMileageSerializer


class MileageListAPIView(generics.ListAPIView):
    queryset = Mileage.objects.all()
    serializer_class = MileageSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['car', 'motorcycle']
    ordering_fields = ['year']
