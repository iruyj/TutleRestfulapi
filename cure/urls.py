from django.urls import path, include
from django.conf.urls import url
from cure import views

app_name = "cures"
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('cures/',views.cures_list),
]