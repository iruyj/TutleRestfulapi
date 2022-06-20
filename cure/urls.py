from django.urls import path, include
from django.conf.urls import url
from cure import views
# from cure.views import all_log

app_name = "cures"
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('user',views.CureUser.as_view(),name='cures_user'),
    path('date',views.DaysSelect.as_view(),name='cures_day'),
    path('',views.Cures.as_view(),name='cures'),
    path('<int:id>',views.cure_select,name='select'),
    # path('list/',views.CureAll.as_view(),name='list'),
    # path('log/',all_log ,name='all'),
    # path
]