from django.db import models

# Create your models here.
class Combinedmodel(models.Model):
    doctorname=models.CharField(max_length=10)
    patientname=models.CharField(max_length=10)
    did=models.IntegerField(max_length=4,default=0)
    pid=models.IntegerField(max_length=4,default=0)

