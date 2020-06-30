from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, UserForm, ProfileForm
from django.contrib.auth import logout
from gym.models import Classes, Profile
from django.views import generic

import json

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.name = form.cleaned_data.get('name')
            user.profile.surname = form.cleaned_data.get('surname')
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('show_profile')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def show_profile(request):
    user_form = UserForm(request.POST, instance=request.user)
    profile_form = ProfileForm(request.POST, instance=request.user.profile)

    allowed_rating = []

    # for clss in profile_form.classes:
    #     if not check_if_rated(request, clss):
    #         allowed_rating.append(clss)

    return render(request, 'show_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
        #'clss': clss
    })


# def check_if_rated(request, class_id):
#     clss = Classes.objects.get(pk=class_id)
#     trainer = clss.trainer.id
#     rates = trainer.rate_set.all()
#     user = Profile.objects.get(pk=request.user.id)
#     rated = False
#     for rate in rates:
#         if(rate.user.id == user.id):
#             rated = True
#     return rated


def drop_from_class(request, class_id):
    my_class = Classes.objects.get(pk=class_id)
    user = Profile.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        user.classes.remove(my_class)
        user.save()
        return redirect('show_profile')
    return render(request, 'drop_class.html', {'my_class': my_class, 'user': user})


def logout_view(request):
    logout(request)
    return redirect('index')
