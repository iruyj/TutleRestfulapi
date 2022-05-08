from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from cure import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^cure/', include('cure.urls'),name='cure'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]