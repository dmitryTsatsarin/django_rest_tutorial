from rest_framework.test import APITestCase
from rest_framework import status as rest_status

from main_app import factories
from main_app.models import Artist


class App3TestCase(APITestCase):
    def setUp(self):
        pass

    def test_ok(self):
        artist = factories.ArtistFactory.create(first_name='Vera')
        print Artist.objects.get().first_name
        data_in = {
            'first_name': 'Ivan',
            'age': 37
        }
        response = self.client.put('/api/app3/%s' % artist.pk, data=data_in, format='json')
        print response.content
        self.assertEqual(response.status_code, rest_status.HTTP_200_OK)
        print Artist.objects.get().first_name
