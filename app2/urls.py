# -*- coding: utf-8 -*-
__author__ = 'forward'

from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.App2View.as_view()),
]
