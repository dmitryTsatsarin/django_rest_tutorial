from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^api/app1', include('app1.urls')),
    url(r'^api/app2', include('app2.urls')),
    url(r'^api/app3/', include('app3.urls')),
    url(r'^api/app4/', include('app4.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
