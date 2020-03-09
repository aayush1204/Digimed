
# Create your views here.


from django.shortcuts import render
import requests
from django.http import HttpResponse
from home2.models import Appointmentmodel,MedicalRecord
from django.views.generic import TemplateView
from home2.forms import fileuploadform
# Create your views here.
def home1(request):
    pid=1
    dc=Appointmentmodel.objects.filter(flag="1")

    return render(request,"patientdash.html",{'dc':dc,'pid':pid})
def home3(request):

    dc=Appointmentmodel.objects.filter(flag="1")

    return render(request,"patientdash.html",{'dc':dc,})

def add1(request):
    db=Appointmentmodel.objects.all()

    return render(request,"aww.html",{'db':db})
    # return HttpResponse(db.doctor_name)

# def med2(request):
#     ds=MedicalRecord.objects.all()
def appbook(request):
    spec=request.GET['data2']
    docn=request.GET['data1']
    db=Appointmentmodel.objects.get(doctor_name=docn)
    return render(request, "bookapp.html",{'db':db,})

def conbook(request, p):
    time=request.GET['time']
    d=request.GET['date1']
    doc= Appointmentmodel.objects.filter(did=p)
    t1="0"
    t2="0"
    t3="0"
    t4="0"
    t5="0"
    t6="0"

    if time=="timingslot1":
        t1="1"
    if time=="timingslot2":
        t2="1"
    if time=="timingslot3":
        t3="1"
    if time=="timingslot4":
        t4="1"
    if time=="timingslot5":
        t5="1"
    if time=="timingslot6":
        t6="1"
    doc.update(timingslot1=t1,timingslot2=t2,timingslot3=t3,timingslot4=t4,timingslot5=t5,timingslot6=t6,flag="1",date=d)
    dc= Appointmentmodel.objects.filter(did=p)
    # doc.save()
    return render(request,"conbook.html",{'dc':dc,})
def readingfile(request):
    modelinstance=MedicalRecord.objects.filter(pid='1').last()
    s2=modelinstance.filename
    #return HttpResponse(s2)
    s1=r"A:\digimed\media"+"\\"
    s3=s1+s2
    f=open(s3,'r')
    #return render(request,"medrec.html")
    return HttpResponse(s3)
class medreccall(TemplateView):
        def get(self,request):
            forminput=fileuploadform()
            return render(request,"medrec.html",{'forminput':forminput,})
        def post(self,request):
            forminput=fileuploadform(request.POST,request.FILES)
            text="Succesful Upload"
            text2="View Uploaded File"
            obj=home1(request)
            if forminput.is_valid():
                date=forminput.cleaned_data['date']
                uploadedfile=request.FILES['files']
                # filename=uploadedfile.files.name
                modelinstance=MedicalRecord.objects.create(date=date,files=uploadedfile,pid=1,patient_name="Dhruvi")

            #return HttpResponse(modelinstance.files.name)
            return render(request,"medrec.html",{'text':text,"ViewFiles":text2,})
            # return  HttpResponse()

