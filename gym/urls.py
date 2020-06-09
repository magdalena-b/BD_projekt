from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from . import views



urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('gym/trainers/<trainer_id>/', views.trainers_details, name='trainers_details'),
    path('gym/classes/<class_id>/', views.classes_details, name='classes_details'),
    path('gym/registration', views.UserFormView.as_view(), name='user_form')
    #path('gym/trainers/<trainer_id>/', views.TrainersDetailsView.as_view(), name='trainers_details'),
    #path('gym/classes/<int:class_id>/', views.ClassesDetailsView.as_view(), name='classes_details'),
    #url(r'(^gym/classes/(?P<pk>\d+)/$)|(^gym/classes/(?P<product_slug>\w+)/$)', views.ClassesDetailsView.as_view(), name='classes_details'),
    #url(r'(^gym/classes/(?P<pk>\d+)/$)', views.ClassesDetailsView.as_view(), name='classes_details'),
    #url(r'gym/trainers/(?P<trainer_id>\d+)/$', views.TrainersDetailsView.as_view(), name='trainers_details'),
    #path('gym/classes/<class_id>/', views.classes_details, name='classes_details')
]
