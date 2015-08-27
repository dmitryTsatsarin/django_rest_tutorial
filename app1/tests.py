from rest_framework.test import APITestCase
from rest_framework import status as rest_status


class App1TestCase(APITestCase):
    def setUp(self):
        pass

    def test_ok(self):
        response = self.client.get('/api/app1', {}, format='json')
        self.assertEqual(response.status_code, rest_status.HTTP_200_OK)
        print response.content
