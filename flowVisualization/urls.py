from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^clearCache', views.clrCache, name='clearCache'),
    url(r'^createRecord', views.createRecord, name='createRecord'),
    url(r'^staticChart', views.viewStaticCharts, name='staticChart')
]