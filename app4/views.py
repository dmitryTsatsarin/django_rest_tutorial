# -*- coding: utf-8 -*-

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin, CreateModelMixin, ListModelMixin

from serializers import ArtistSerializer, ArtistListSerializer
from main_app.models import Artist



# Усложнение. POST и PUT Минимальное использование своего кода
#             GET - использование сериализатора для выходных данных

class App4View(CreateModelMixin, UpdateModelMixin, ListModelMixin, GenericAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.filter()

    def perform_create(self, serializer):
        return Artist.objects.create(**serializer.validated_data)

    def perform_update(self, serializer):
        artist = self.get_object()
        artist.__dict__.update(serializer.validated_data)
        return artist.save()

    def post(self, request, **kwargs):
        return self.create(request, **kwargs)

    def put(self, request, **kwargs):
        return self.update(request, **kwargs)


    def get(self, request, **kwargs):
        self.serializer_class = ArtistListSerializer
        return self.list(request, **kwargs)