# -*- coding: utf-8 -*-
__author__ = 'forward'

from rest_framework import serializers


class CreateArtistSerializer(serializers.Serializer):
    age = serializers.IntegerField()
    first_name = serializers.CharField(max_length=255)
