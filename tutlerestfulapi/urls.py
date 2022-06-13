from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.models import User

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    url('cure/', include('cure.urls'),name='cure'),
    url('turtle/', include('turtles.urls'),name='turtle'),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]