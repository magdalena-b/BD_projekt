from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Trainer, Classes


def index(request):
    all_trainers = Trainer.objects.all()
    all_classes = Classes.objects.all()
#    template = loader.get_template('gym/index.html')
    context = {
        'all_trainers': all_trainers,
        'all_classes': all_classes
    }

#     html = ''
#     for trainer in all_trainers:
#         url = '/gym/' + str(trainer.id) + '/'
#         html += '<a href="' + url + '">' + trainer.surname + '</a><br>'

 #   return HttpResponse(template.render(context, request))
    return render(request, 'gym/index.html', context)



def trainers_details(request, trainer_id):
    return HttpResponse("<h2> Details for Trainer ID: " + str(trainer_id) +  "</h2>")




def classes_details(request, class_id):
    
    clss = Classes.objects.get(pk=class_id)
    return render(request, 'gym/classes_details.html', {'class': clss})
 
 #   return HttpResponse("<h2> Details for: " + str(class_id) + "</h2>")