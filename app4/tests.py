from rest_framework.test import APITestCase
from rest_framework import status as rest_status

from main_app import factories
from main_app.models import Artist


class App4TestCase(APITestCase):
    def setUp(self):
        pass

    def test_ok_create(self):
        data_in = {
            'first_name': 'Ivan',
            'age': 37
        }

        response = self.client.post('/api/app4/', data=data_in, format='json')
        self.assertEqual(response.status_code, rest_status.HTTP_201_CREATED)
        print Artist.objects.values()

    def test_ok_update(self):
        artist = factories.ArtistFactory.create(first_name='Vera', age=50)
        data_in = {
            'first_name': 'Elena',
            'age': 18
        }

        response = self.client.put('/api/app4/%s' % artist.pk, data=data_in, format='json')
        self.assertEqual(response.status_code, rest_status.HTTP_200_OK)
        print 'Database result is %s' % Artist.objects.values()

    def test_ok_get_list(self):
        factories.ArtistFactory.create(first_name='Vera', last_name='Prohorova', age=50)
        factories.ArtistFactory.create(first_name='Miha', last_name='Arafat', age=20)
        factories.ArtistFactory.create(first_name='some fellow', last_name='bla bla bla', age=25)

        response = self.client.get('/api/app4/', {}, format='json')
        self.assertEqual(response.status_code, rest_status.HTTP_200_OK)
        print response.content


