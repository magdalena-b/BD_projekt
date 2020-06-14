from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from gym.models import Profile

class SignUpForm(UserCreationForm):

    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    name = forms.CharField(max_length=254, required=True)
    surname = forms.CharField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'name', 'surname', 'email', 'password1', 'password2')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'surname', 'classes')






# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# #from django.contrib.auth.models import User
# from gym.models import User


# class SignUpForm(UserCreationForm):
#     email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
#     name = forms.CharField(max_length=254, required=True)
#     surname = forms.CharField(max_length=254, required=True)

#     class Meta:
#         model = User
#         fields = ('username', 'name', 'surname', 'email', 'password1', 'password2')

