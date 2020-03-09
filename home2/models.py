from django.db import models

# Create your models here.
class Appointmentmodel(models.Model):
    did=models.IntegerField(default=0)
    doctor_name=models.CharField(max_length=30)
    speciality = models.CharField(max_length=20)
    timingslot1 = models.IntegerField(default=0)
    timingslot2 = models.IntegerField(default=0)
    timingslot3 = models.IntegerField(default=0)
    timingslot4 = models.IntegerField(default=0)
    timingslot5 = models.IntegerField(default=0)
    timingslot6 = models.IntegerField(default=0)
    flag= models.IntegerField(default=0)
    date=models.CharField(max_length=12,default="11/10/2019")
    # timingslot1time = models.CharField(default="10:00-11:00pm")
    # timingslot2time = models.CharField(default="11:00-12:00pm")
    # timingslot3time = models.CharField(default="12:00-1:00pm")
    # timingslot4time = models.CharField(default="")
    # timingslot5time = models.CharField(default="")
    # timingslot6time = models.CharField(default="")


class MedicalRecord(models.Model):
    patient_name=models.CharField(max_length=30)
    pid=models.IntegerField(default=0)
    date= models.DateField(default="2019-10-11")
    files=models.FileField(upload_to='media')
    filename=models.CharField(max_length=100)