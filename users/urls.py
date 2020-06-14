from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views




urlpatterns = [
    path('register/signup', views.signup, name='signup'),
    #path('register/login', auth_views.login, name='login')
    path('login/', LoginView.as_view(), name='login'),
    path('profile', views.show_profile, name='show_profile')

]