from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from . import views



urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('gym/trainers/<trainer_id>/', views.trainers_details, name='trainers_details'),
    path('gym/classes/<class_id>/', views.classes_details, name='classes_details'),
    path('gym/favourited/<class_id>', views.favourited, name='favourited'),]
