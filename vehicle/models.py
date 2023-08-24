from django.db import models
from django.conf import settings


class Car(models.Model):
    model = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    year = models.PositiveSmallIntegerField(default=0, verbose_name='год')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.model}'

    class Meta:
        verbose_name = 'автомобиль'
        verbose_name_plural = 'автомобили'


class Motorcycle(models.Model):
    model = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    year = models.PositiveSmallIntegerField(default=0, verbose_name='год')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.model}'

    class Meta:
        verbose_name = 'мотоцикл'
        verbose_name_plural = 'мотоциклы'


class Mileage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True, null=True, related_name='mileage')
    motorcycle = models.ForeignKey(Motorcycle, on_delete=models.CASCADE, blank=True, null=True, related_name='mileage')

    year = models.PositiveSmallIntegerField(default=0, verbose_name='год регистрации пробега')
    mileage = models.PositiveIntegerField(default=0, verbose_name='пробег')

    def __str__(self):
        return f'{self.car if self.car else self.motorcycle} - {self.mileage} ({self.year})'

    class Meta:
        verbose_name = 'пробег'
        verbose_name_plural = 'пробеги'
        ordering = ('-year',)
