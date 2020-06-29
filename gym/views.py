from datetime import datetime, date, time
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views import generic
from django.views.generic.edit import CreateView
from .templates.gym.forms import UserForm, AddRateForm
from .models import Trainer, Classes, Profile, Rate

# def index(request):

#     all_trainers = Trainer.objects.all()
#     all_classes = Classes.objects.all()
#     context = {
#         'all_trainers': all_trainers,
#         'all_classes': all_classes
#     }

#     return render(request, 'gym/index.html', context)


class IndexView(generic.ListView):
    template_name = 'gym/index.html'
    def get_queryset(self):
        now = datetime.now()
        future_filter = Classes.objects.filter(date__gte=now)
        return future_filter

    # def get_queryset(self):
    #     return Classes.objects.raw('SELECT * FROM gym_classes where date > current_date order by date ')


def current_date(request):
    now = datetime.time.now()
    print("Date: "+ now.strftime("%Y-%m-%d"))


def trainers_details(request, trainer_id):

    trainer = Trainer.objects.get(pk=trainer_id)
    return render(request, 'gym/trainers_details.html', {'trainer': trainer})


def classes_details(request, class_id):
    
    clss = Classes.objects.get(pk=class_id)
    trainer = Trainer.objects.get(pk=clss.trainer.id)
    #user = Profile.objects.get(user_id=request.user.id)
    #user.classes.clear()
    #user.save()
    return render(request, 'gym/classes_details.html', {'clss': clss, 'trainer': trainer})


def favourited(request, class_id):
    clss = Classes.objects.get(pk=class_id)
    user = Profile.objects.get(user_id=request.user.id)
    user.classes.add(clss)
    user.save()
    return render(request, 'gym/index.html')


class ClassCreate(CreateView):
    model = Classes
    template_name = 'gym/classes_form.html'
    fields = ['trainer', 'date', 'name', 'description']


class UserFormView(View):
    form_class = UserForm
    template_name = 'gym/registration_form.html'

    def get(self, request): # display blank form
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request): # proccess form data
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned/normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save() # saves to the database

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('gym:index')

        return render(request, self.template_name, {'form': form})


def add_rate(request, trainer_id):
    if request.method == 'POST':
        form = AddRateForm(request.POST)
        if form.is_valid():
            Rate.objects.create(
                user=Profile.objects.get(user=request.user.id),
                rate=form.cleaned_data['rate'],
                trainer=Trainer.objects.get(pk=trainer_id),
            )
            return HttpResponseRedirect(f'/accounts/profile')
    else:
        form = AddRateForm()

    return render(request, 'gym/add_rate.html', {'form': form})

