from rest_framework import serializers

from vehicle.models import Car, Motorcycle, Mileage


class MileageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mileage
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    last_mileage = serializers.IntegerField(source='mileage_set.last.mileage', default=0, read_only=True)

    # mileage_set это queryset, т.е. набор данных;
    # last/first это либо последние данные, либо первые зависит от ordering в модели Mileage;
    # mileage обращение к полю модели mileage
    # default базовое значение
    # read_only если мы хотим эти данные генерировать только для выдачи

    # для вывода всех пробегов реализуем переменную mileage куда передаем сериализатор CarMileageSerializer
    # many=True для вывода всех пробегов
    # read_only чтобы можно было далее заполнять без необходимости указывать пробег
    # source='mileage_set' для передачи queryset (ссылка из пробега на машину)

    class Meta:
        model = Car
        fields = '__all__'


class MotorcycleSerializer(serializers.ModelSerializer):
    last_mileage = serializers.SerializerMethodField()

    class Meta:
        model = Motorcycle
        fields = '__all__'

    def get_last_mileage(self, instance):
        mileage = instance.mileage_set.all().last()
        if mileage:
            return mileage.mileage
        return 0
