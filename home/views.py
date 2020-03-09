from django.shortcuts import render
import requests
from django.http import HttpResponse
from home.forms import loginpatientform,logindoctorform,registerpatientform,registerdoctorform
from django.views.generic import TemplateView
from home.models import Patientmodel,Doctormodel,temppatientmodel,tempdoctormodel
# Create your views here.
def displayout(request):
    return render(request,'events1.html')

def  displayout1(request):
    return render(request,'events2.html')
def first(request):
    return render(request,'ACEADAA.html')
def regchoice(request):
    return render(request,'regchoice.html')
def creating(request):
    cho=request.GET['dp']

    if cho == 'doctor':
        forminput=registerdoctorform()
        return render(request,'register.html',{'forminput':forminput})
    else:
        forminput=registerpatientform()
        return render(request,'register.html',{'forminput':forminput})
    return render(request,'ACEADAA.html')
# def login(request):
#     return render(request,'login1.html')
# def firstpage(request):
#     if request.method == 'POST':
#         docid= request.POST.get('user1')
#         pass1=request.POST.get('password')
#         docs= Doctormodel.objects.filter(did=docid)
#         docname=Doctormodel.objects.get(did=docid).name
#     # if(docs == None):
#     #     return render(request, 'login1.html')
#         if docs.password == pass1:
#             return render(request,'afterlogin1.html',{'did':docid,'docname':docname})
#     return HttpResponse("FAILED")
# class logintry(TemplateView):
#     def get(self,request):
#             return render(request,'login1.html')
    
#     def post(self,request):
#         docid= request.GET['user1']
#         pass1=request.GET['password']
#         docs= DoctorModel.objects.filter(did=docid)
#         docname=Doctormodel.objects.get(did=docid).name
#         if(docs == None):
#             return render(request, 'login1.html')
#         if docs.password == pass1:
#             return render(request,'afterlogin1.html',{'did':docid,'docname':docname})

class homepage(TemplateView):
    text="Patient Login"
    def get(self,request):
        #if request=="GET":
            forminput=loginpatientform()
            return render(request,'home.html',{'forminput':forminput})
        #if request == "POST":  
    def post(self,request):
        forminput=loginpatientform(request.POST)
        if forminput.is_valid():
            
            patientid=forminput.cleaned_data['pid']
            password=forminput.cleaned_data['password']
            dbpid= Patientmodel.objects.get(pid=patientid)

            if dbpid == None:
                return render(request,'home.html',{'text':self.text})
            elif dbpid.password == password:
                #modelinstance=Patientmodel.objects.create(pid = patientid,  )
                modelinstance=temppatientmodel.objects.create(pid=patientid)
                return render(request, 'patientdash.html')
            else:
                return render(request,'home.html',{'forminput':loginpatientform(),'text':self.text})    #return render(request,'home.html',{'forminput':forminput})
        return render(request,'home.html',{'forminput':loginpatientform(),'text':self.text})

class homepage2(TemplateView):
    text = "Doctor Login"
    def get(self,request):
        forminput=logindoctorform()
        return render(request,'home.html',{'forminput':forminput,'text':self.text})
    def post(self,request):
        forminput=logindoctorform(request.POST)
        if forminput.is_valid():
            doctorid=forminput.cleaned_data['did']
            password=forminput.cleaned_data['password']
            docid=Doctormodel.objects.get(did=doctorid).did
            docname=Doctormodel.objects.get(did=doctorid).name
            dbdid= Doctormodel.objects.get(did=doctorid)
            
            if dbdid == None:
                return render(request,'home.html',{'forminput':logindoctorform(),'text':self.text})
            elif dbdid.password == password:
                #modelinstance=Patientmodel.objects.create(pid = patientid,  )
                modelinstance=tempdoctormodel.objects.create(did=docid)
                return render(request,'afterlogin1.html',{'did':docid,'docname':docname})
            else:
                return render(request,'home.html',{'forminput':logindoctorform(),'text':self.text})    #return render(request,'home.html',{'forminput':forminput})
        return render(request,'home.html',{'forminput':logindoctorform(),'text':self.text})

class patientregister(TemplateView):
    def post(self,request):
    #     forminput=registerpatientform()
    #     return render(request,'register.html',{'forminput':forminput})
    # def post(self,request):

            forminput=registerpatientform(request.POST)
            if forminput.is_valid():
                patientid=forminput.cleaned_data['pid']
                password=forminput.cleaned_data['password']
                name=forminput.cleaned_data['name']
            modelinstance=Patientmodel.objects.create(pid= patientid,password=password,name=name)
            return HttpResponse("Done")
class doctorregister(TemplateView):
    def get(self,request):
        forminput=registerdoctorform()
        return render(request,'register.html',{'forminput':forminput})
    def post(self,request):
        forminput=registerdoctorform(request.POST)
        if forminput.is_valid():
            doctorid=forminput.cleaned_data['did']
            password=forminput.cleaned_data['password']
            name=forminput.cleaned_data['name']
        modelinstance=Doctormodel.objects.create(did= doctorid,password=password,name=name)
        return HttpResponse("Done")

# from django.shortcuts import render
# import requests
# from django.http import HttpResponse
# from home2.models import Appointmentmodel,MedicalRecord
# from django.views.generic import TemplateView
# from home2.forms import fileuploadform
# # Create your views here.
# def home1(request):
#     pid=1
#     dc=Appointmentmodel.objects.filter(flag="1")

#     return render(request,"patientdash.html",{'dc':dc,'pid':pid})
# def home3(request):

#     dc=Appointmentmodel.objects.filter(flag="1")

#     return render(request,"patientdash.html",{'dc':dc,})

# def add1(request):
#     db=Appointmentmodel.objects.all()

#     return render(request,"aww.html",{'db':db})
#     # return HttpResponse(db.doctor_name)

# # def med2(request):
# #     ds=MedicalRecord.objects.all()
# def appbook(request):
#     spec=request.GET['data2']
#     docn=request.GET['data1']
#     db=Appointmentmodel.objects.get(doctor_name=docn)
#     return render(request, "bookapp.html",{'db':db,})

# def conbook(request, p):
#     time=request.GET['time']
#     d=request.GET['date1']
#     doc= Appointmentmodel.objects.filter(did=p)
#     t1="0"
#     t2="0"
#     t3="0"
#     t4="0"
#     t5="0"
#     t6="0"

#     if time=="timingslot1":
#         t1="1"
#     if time=="timingslot2":
#         t2="1"
#     if time=="timingslot3":
#         t3="1"
#     if time=="timingslot4":
#         t4="1"
#     if time=="timingslot5":
#         t5="1"
#     if time=="timingslot6":
#         t6="1"
#     doc.update(timingslot1=t1,timingslot2=t2,timingslot3=t3,timingslot4=t4,timingslot5=t5,timingslot6=t6,flag="1",date=d)
#     dc= Appointmentmodel.objects.filter(did=p)
#     # doc.save()
#     return render(request,"conbook.html",{'dc':dc,})
# def readingfile(request):
#     modelinstance=MedicalRecord.objects.filter(pid='1').last()
#     s2=modelinstance.filename
#     #return HttpResponse(s2)
#     s1=r"A:\digimed\media"+"\\"
#     s3=s1+s2
#     f=open(s3,'r')
#     #return render(request,"medrec.html")
#     return HttpResponse(s3)
# class medreccall(TemplateView):
#         def get(self,request):
#             forminput=fileuploadform()
#             return render(request,"medrec.html",{'forminput':forminput,})
#         def post(self,request):
#             forminput=fileuploadform(request.POST,request.FILES)
#             text="Succesful Upload"
#             text2="View Uploaded File"
#             obj=home1(request)
#             if forminput.is_valid():
#                 date=forminput.cleaned_data['date']
#                 uploadedfile=request.FILES['file']
#                 filename=uploadedfile.files.name
#                 modelinstance=MedicalRecord.objects.create(date=date,files=uploadedfile,pid=1,patient_name="Dhruvi",filename=filename)

#             #return HttpResponse(modelinstance.files.name)
#             return render(request,"medrec.html",{'text':text,"ViewFiles":text2,"filename":filename})
#             # return  HttpResponse()


