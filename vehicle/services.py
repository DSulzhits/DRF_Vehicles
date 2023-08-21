import requests
from rest_framework import status
from django.conf import settings


def convert_currencies(rub_price):
    usd_price = 0
    response = requests.get(
        f'{settings.CURRENCY_API_URL}v3/latest?apikey={settings.CURRENCY_API_KEY}&currencies=RUB'
    )
    if response.status_code == status.HTTP_200_OK:
        usd_rate = response.json()['data']['RUB']['value']
        usd_price = rub_price / usd_rate

    return round(usd_price, 2)
