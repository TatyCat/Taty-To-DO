from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.todo, name='todo'),
    url(r'^new_todo/$', views.new_todo, name='new_todo'),
]
