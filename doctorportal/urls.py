from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views
#from doctorportal.views import *
from home.views import homepage,homepage2,patientregister,doctorregister
urlpatterns = [
    
    
    #url('direct1/',views.doctordashboard,name='direct1'), 
    path('direct1/',views.patientlist,name='direct1'),
    path('det/<int:p>',views.detail,name="det"),
    path('upcapp/',views.upcapp,name="upcapp"),
    #url('home2/',homepage.as_view(),name='home2'),
    #url('',views.first,name='first'),
    #path('',homepage2.as_view(),name='home2'),

]