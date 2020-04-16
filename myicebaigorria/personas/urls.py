from django.urls import path
from . import views

urlpatterns = [
    path('', views.personas_list, name='personas_list'),
]