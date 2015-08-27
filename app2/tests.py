from rest_framework.test import APITestCase
from rest_framework import status as rest_status


class App2TestCase(APITestCase):
    def setUp(self):
        pass

    def test_ok(self):
        data_in = {
            'first_name': 'Ivan',
            'age': 37
        }
        response = self.client.post('/api/app2', data=data_in, format='json')
        print response.content
        self.assertEqual(response.status_code, rest_status.HTTP_201_CREATED)

    def test_fail(self):
        data_in = {
            'first_name': 'Ivan',
            'age': 'I am too old'
        }
        response = self.client.post('/api/app2', data=data_in, format='json')
        print response.content
        self.assertEqual(response.status_code, rest_status.HTTP_400_BAD_REQUEST)
