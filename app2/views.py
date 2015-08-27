# -*- coding: utf-8 -*-

from rest_framework.generics import GenericAPIView
from rest_framework import status as rest_status

from main_app.helpers import JSONResponse
from serializers import CreateArtistSerializer
from main_app.models import Artist



# Рабочий вариант

class App2View(GenericAPIView):
    def get(self, request, **kwargs):
        return JSONResponse({'Hello Leverx'}, status=rest_status.HTTP_200_OK)

    def post(self, request, **kwargs):
        data = request.data
        serializer = CreateArtistSerializer(data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            Artist.objects.create(**validated_data)
            return JSONResponse({'info': 'Всё правильно сделал'}, status=rest_status.HTTP_201_CREATED)
        else:
            return JSONResponse(serializer.errors, status=rest_status.HTTP_400_BAD_REQUEST)
