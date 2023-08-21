from rest_framework import status
from rest_framework.test import APITestCase

from vehicle.models import Motorcycle


class VehicleTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_motorcycle(self):
        """Тестирование создания мотоцикла"""
        data = {
            'model': 'Test',
            'description': 'Test-description',
            'year': 2023
        }

        """Тестирования создания мотоцикла"""
        response = self.client.post(
            '/api/motorcycles/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'last_mileage': 0, 'model': 'Test', 'description': 'Test-description', 'year': 2023,
             'owner': None}
        )

        self.assertTrue(
            Motorcycle.objects.all().exists()
        )

    def test_list_motorcycle(self):
        """Тестирование вывода списка мотоциклов"""
        Motorcycle.objects.create(
            model='list_test',
            description='list_test_description',
            year=2023
        )

        response = self.client.get(
            '/api/motorcycles/',
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": 2,
                        "last_mileage": 0,
                        "model": "list_test",
                        "description": "list_test_description",
                        "year": 2023,
                        "owner": None
                    }
                ]
            }
        )
