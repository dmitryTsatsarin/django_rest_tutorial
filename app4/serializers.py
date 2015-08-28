# -*- coding: utf-8 -*-
__author__ = 'forward'

from rest_framework import serializers


class ArtistSerializer(serializers.Serializer):
    age = serializers.IntegerField()
    first_name = serializers.CharField(max_length=255)


class ArtistListSerializer(serializers.Serializer):
    age = serializers.IntegerField()
    first_name = serializers.CharField(max_length=255)
    me_renamed_field = serializers.CharField(max_length=255, source='last_name')
