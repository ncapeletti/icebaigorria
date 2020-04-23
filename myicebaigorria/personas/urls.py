from django.urls import path
from . import views

urlpatterns = [
    path('', views.personas_list, name='personas_list'),
    path('persona/<int:pk>/', views.persona_detail, name='persona_detail'),
    path('persona/new', views.persona_new, name='persona_new'),
    path('persona/<int:pk>/edit/', views.persona_edit, name='persona_edit'),
]

