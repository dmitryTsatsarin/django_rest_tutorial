# -*- coding: utf-8 -*-
__author__ = 'forward'

from django.conf.urls import url

import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)?', views.App4View.as_view()),
]
