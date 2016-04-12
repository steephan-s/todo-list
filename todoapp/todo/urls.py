from django.conf.urls import url
from . import views

app_name = 'todo'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^push_function/$', views.push_function, name='push_function'),
    url(r'^(?P<pk>\d+)/delete/$', views.delete_function, name='delete'),
    url(r'^(?P<pk>\d+)/add/$', views.add_function, name='add'),
    url(r'^(?P<pk>\d+)/remove/$', views.remove_function, name='remove'),
]
