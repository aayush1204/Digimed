from django.db import models

# Create your models here.
class Patientmodel(models.Model):
    pid=models.CharField(max_length=4)
    password=models.CharField(max_length=100)
    name = models.CharField(max_length=100)
class Doctormodel(models.Model):
    did=models.CharField(max_length=4)
    password=models.CharField(max_length=100)
    name=models.CharField(max_length=100,default='no')
class temppatientmodel(models.Model):
    pid=models.IntegerField(max_length=4)
class tempdoctormodel(models.Model):
    did=models.IntegerField(max_length=4,default=0)