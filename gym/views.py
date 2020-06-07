from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Trainer



# def index(request):
#     return render(request, 'gym/index.html')


def index(request):
    all_trainers = Trainer.objects.all()
    template = loader.get_template('gym/index.html')
    context = {
        'all_trainers': all_trainers
    }

#     html = ''
#     for trainer in all_trainers:
#         url = '/gym/' + str(trainer.id) + '/'
#         html += '<a href="' + url + '">' + trainer.surname + '</a><br>'

    return HttpResponse(template.render(context, request))

    # return HttpResponse("Hello, world. You're at the gym index.")


def trainers_details(request, trainer_id):
    return HttpResponse("<h2> Details for Trainer ID: " + str(trainer_id) +  "</h2>")