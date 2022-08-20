from django.urls import path, include, re_path
from first_app import views


urlpatterns = [

path('', views.index, name='index'),
]
