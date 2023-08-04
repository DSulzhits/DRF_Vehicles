from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    year = models.PositiveSmallIntegerField(default=0, verbose_name='год')

    def __str__(self):
        return f'{self.model}'

    class Meta:
        verbose_name = 'автомобиль'
        verbose_name_plural = 'автомобили'


class Motorcycle(models.Model):
    model = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    year = models.PositiveSmallIntegerField(default=0, verbose_name='год')

    def __str__(self):
        return f'{self.model}'

    class Meta:
        verbose_name = 'мотоцикл'
        verbose_name_plural = 'мотоциклы'


class Mileage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True, null=True)
    motorcycle = models.ForeignKey(Motorcycle, on_delete=models.CASCADE, blank=True, null=True)

    year = models.PositiveSmallIntegerField(default=0, verbose_name='год регистрации пробега')
    mileage = models.PositiveIntegerField(default=0, verbose_name='пробег')

    def __str__(self):
        return f'{self.car if self.car else self.motorcycle} - {self.mileage} ({self.year})'

    class Meta:
        verbose_name = 'пробег'
        verbose_name_plural = 'пробеги'
        ordering = ('year',)
