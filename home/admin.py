from django.contrib import admin
from home.models import  Patientmodel,Doctormodel
from doctorportal.models import Combinedmodel
# Register your models here.
admin.site.register(Patientmodel),
admin.site.register(Doctormodel),
admin.site.register(Combinedmodel)