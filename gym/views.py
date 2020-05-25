from django.shortcuts import render
from django.http import HttpResponse
from .models import Trainer


def index(request):
    all_trainers = Trainer.objects.all()
    html = ''
    for trainer in all_trainers:
        url = '/gym/' + str(trainer.id) + '/'
        html += '<a href="' + url + '">' + trainer.surname + '</a><br>'

    return HttpResponse(html)

#    return HttpResponse("Hello, world. You're at the gym index.")


def trainers_details(request, trainer_id):
    return HttpResponse("<h2> Details for Trainer ID: " + str(trainer_id) +  "</h2>")