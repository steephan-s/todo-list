from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'todo'
urlpatterns = [
    url(r'^$', views.index.as_view(), name='index'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
