# tutlerestfulapi/urls.py
from django.contrib import admin
from django.urls import path, include

from turtles import views

urlpatterns = [
    path('connect/',views.TurtleLogin.as_view(),name='connect'),
    path('new/',views.CreateTurtle.as_view(),name='new')
]