# -*- coding: utf-8 -*-

from rest_framework.generics import GenericAPIView
from rest_framework import status as rest_status

from main_app.helpers import JSONResponse
from serializers import ArtistSerializer
from main_app.models import Artist



# Усложнение. Использование конструкций django-rest-framework

class App3View(GenericAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.filter()

    def put(self, request, **kwargs):
        """
        Object update
        """
        data = request.data
        serializer = self.get_serializer(data=data)
        artist = self.get_object()
        if serializer.is_valid():
            validated_data = serializer.validated_data
            artist.__dict__.update(validated_data)
            artist.save()
            return JSONResponse({'info': 'Ай маладэц'}, status=rest_status.HTTP_200_OK)
        else:
            return JSONResponse(serializer.errors, status=rest_status.HTTP_400_BAD_REQUEST)

    def get(self, request, **kwargs):
        pass

    def post(self, request, **kwargs):
        pass

    def delete(self, request, **kwargs):
        pass
