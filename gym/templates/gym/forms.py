from django.contrib.auth.models import User
from django import forms

RATES_OPTIONS = (
    (1, 'Bad trainer'),
    (2, 'Not good trainer'),
    (3, 'Not bad trainer'),
    (4, 'Good trainer'),
    (5, 'Very good trainer'),
)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class AddRateForm(forms.ModelForm):
    rate = forms.CharField(widget=forms.Select(choices=RATES_OPTIONS),)

    class Meta:
        model = User
        fields = ['rate']

