from django.urls import path
from tours import views

from .schema import schema

urlpatterns = [
    path('', views.index, name='index'),
]