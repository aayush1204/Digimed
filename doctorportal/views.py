from django.shortcuts import render
from home.models import Doctormodel,tempdoctormodel
# from 
from django.http import HttpResponse
from doctorportal.models import Combinedmodel
from home2.models import MedicalRecord, Appointmentmodel

# # Create your views here.
def patientlist(request,):
    doctor_id=tempdoctormodel.objects.last().did

    db= Combinedmodel.objects.filter(did=doctor_id)
    d=db.last()
    doctor_name=d.doctorname
    s="List of Patients:"
    return render(request,'afterlogin1.html',{'s':s,'patients':db,'docname':doctor_name,'did':doctor_id})

def detail(request, p):
    s=Combinedmodel.objects.filter(pid=p).last()
    patient_name=s.patientname
    
    db=MedicalRecord.objects.filter(pid=p)

    doctor_id=tempdoctormodel.objects.last().did

    dc= Combinedmodel.objects.filter(did=doctor_id)
    d=dc.last()
    doctor_name=d.doctorname
    return render(request,'detailrec.html',{'patient_name':patient_name,'db':db,'docname':doctor_name,})

def upcapp(request, ):
    s=Appointmentmodel.objects.filter(flag="1")
    doctor_id=tempdoctormodel.objects.last().did

    dc= Combinedmodel.objects.filter(did=doctor_id)
    d=dc.last()
    doctor_name=d.doctorname
    return render(request, 'upcapp.html',{'db':s,'docname':doctor_name,})

