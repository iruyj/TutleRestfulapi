from django.urls import path, include
from django.conf.urls import url
from cure import views
from cure.views import all_log

app_name = "cures"
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('cures/user/',views.CureSelect.as_view(),name='cures_user'),
    # path('cures/today/',views.TodaySelect.as_view(),name='cures_today'),
    # path('new/',views.CureCreate.as_view(),name='new'),
    path('log/',all_log ,name='all'),
]