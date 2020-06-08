from django.contrib import admin
from django.urls import include, path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('gym/trainers/<trainer_id>/', views.trainers_details, name='trainers_details'),
    path('gym/classes/<class_id>/', views.classes_details, name='classes_details')
]
