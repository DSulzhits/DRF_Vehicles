from django.urls import path

from vehicle.apps import VehicleConfig
from rest_framework.routers import DefaultRouter

from vehicle.views import CarCreateAPIView, CarRetrieveAPIView, CarListAPIView, CarUpdateAPIView, CarDestroyAPIView,\
    MileageCreateAPIView, MotorcycleViewSet

app_name = VehicleConfig.name

router = DefaultRouter()
router.register(prefix=r'motorcycles', viewset=MotorcycleViewSet, basename='motorcycles')

urlpatterns = [
    # Cars
    path('cars/', CarListAPIView.as_view(), name='car_list'),
    path('cars/<int:pk>/', CarRetrieveAPIView.as_view(), name='car_get'),
    path('cars/create/', CarCreateAPIView.as_view(), name='car_create'),
    path('cars/update/<int:pk>/', CarUpdateAPIView.as_view(), name='car_update'),
    path('cars/delete/<int:pk>/', CarDestroyAPIView.as_view(), name='car_delete'),

    # Mileage
    path('mileage/create/', MileageCreateAPIView.as_view(), name='пробег'),

] + router.urls
