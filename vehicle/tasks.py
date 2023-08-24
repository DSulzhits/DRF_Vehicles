from celery import shared_task

from vehicle.models import Car, Motorcycle


@shared_task
def check_mileage(pk, model):
    if model == 'Car':
        instance = Car.objects.filter(pk=pk).first()
    else:
        instance = Motorcycle.objects.filter(pk=pk).first()

    if instance:
        prev_mileage = -1
        for mileage in instance.mileage.all():
            if prev_mileage == -1:
                prev_mileage = mileage.mileage

            else:
                if prev_mileage < mileage.mileage:
                    print("Неверный пробег")
                    break
