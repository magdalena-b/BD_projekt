from django.contrib import admin
from .models import Trainer, Classes, Profile, Rate


admin.site.register(Classes)
admin.site.register(Trainer)
admin.site.register(Profile)
admin.site.register(Rate)

