# -*- coding: utf-8 -*-
__author__ = 'forward'

import factory

from models import Artist, Album


class ArtistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Artist


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album
