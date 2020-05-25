from django.contrib import admin
from django.urls import include, path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('gym/<int:trainer_id>/', views.trainers_details, name='trainers_details')
]