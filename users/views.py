from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm

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
    return render(request, 'show_profile.html')
















# from django.shortcuts import render, redirect
# from django.contrib.auth import login

# from gym.models import User_Account
# from .forms import SignUpForm


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             print(form.cleaned_data['name'])
#             user_account = User_Account(user=user, name=form.cleaned_data['name'], surname=form.cleaned_data['surname'])
#             user_account.save()
#             login(request, user)
#             return redirect('start')
#     else:
#         form = SignUpForm()
#     return render(request, 'register/signup.html', {'form': form})












# from django.shortcuts import render, redirect
# from django.contrib.auth import login

# from home.models import UserData
# from .forms import SignUpForm


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             print(form.cleaned_data['name'])
#             user_data = UserData(username=user, name=form.cleaned_data['name'], surname=form.cleaned_data['surname'],
#                                  current_cvs=[])
#             user_data.save()
#             login(request, user)
#             return redirect('start')
#     else:
#         form = SignUpForm()
#     return render(request, 'accounts/signup.html', {'form': form})