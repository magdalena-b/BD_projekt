from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views import generic
from .templates.gym.forms import UserForm
from .models import Trainer, Classes, User

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
        return Classes.objects.all()



def trainers_details(request, trainer_id):

    trainer = Trainer.objects.get(pk=trainer_id)
    return render(request, 'gym/trainers_details.html', {'trainer': trainer})



def classes_details(request, class_id):
    
    clss = Classes.objects.get(pk=class_id)
    return render(request, 'gym/classes_details.html', {'class': clss})


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