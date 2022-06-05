# tutlerestfulapi/urls.py
from django.contrib import admin
from django.urls import path, include

from turtles import views
from turtles.views import tutleList

urlpatterns = [
    # path('connect/',views.TurtleLogin.as_view(),name='connect'),
    path('', tutleList ,name='list'),
    path('user', views.turtles ,name='login'),
    path('new', views.CreateTurtle.as_view() ,name='new')
]