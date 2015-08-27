# -*- coding: utf-8 -*-
__author__ = 'forward'

import factory

from models import Artist


class ArtistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Artist
