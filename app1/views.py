# -*- coding: utf-8 -*-

from rest_framework.generics import GenericAPIView
from rest_framework import status as rest_status

from main_app.helpers import JSONResponse



# Примитив

class App1View(GenericAPIView):
    def get(self, request, **kwargs):
        return JSONResponse({'Hello Alex Adasenka'}, status=rest_status.HTTP_200_OK)
