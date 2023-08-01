from django.urls import path

from vehicle.apps import VehicleConfig
from rest_framework.routers import DefaultRouter

from vehicle.views import CarViewSet, MotorcycleCreateAPIView, MotorcycleListAPIView, MotorcycleUpdateAPIView, \
    MotorcycleDestroyAPIView, MileageCreateAPIView

app_name = VehicleConfig.name

router = DefaultRouter()
router.register(prefix=r'cars', viewset=CarViewSet, basename='cars')

urlpatterns = [
    # Motorcycle
    path('motorcycle/create/', MotorcycleCreateAPIView.as_view(), name='motorcycle_create'),
    path('motorcycle/', MotorcycleListAPIView.as_view(), name='motorcycle_list'),
    path('motorcycle/<int:pk>/', MotorcycleListAPIView.as_view(), name='motorcycle_get'),
    path('motorcycle/update/<int:pk>/', MotorcycleUpdateAPIView.as_view(), name='motorcycle_update'),
    path('motorcycle/delete/<int:pk>/', MotorcycleDestroyAPIView.as_view(), name='motorcycle_delete'),

    # Mileage
    path('mileage/create/', MileageCreateAPIView.as_view(), name='пробег'),

] + router.urls
