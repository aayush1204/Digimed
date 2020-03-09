from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views
from doctorportal.views import *
from home.views import homepage,homepage2,patientregister,doctorregister
# from home2.views import *
urlpatterns = [
    #path('login/aayush',views.firstpage,name='adduser'),  
    #path('login/',views.login,name='login'),

    
    #url('direct1/',views.doctordashboard,name='direct1'), 
    url('event1/',views.displayout,name="event1"),
    url('event2/',views.displayout1,name="event2"),
    # path('adduser/',views.firstpage,name='adduser'),    
    url('home1/',homepage2.as_view(),name='home1'),
    url('reg/',views.regchoice,name='reg'),
    url('finalcho',views.creating,name="finalcho"),
    url('plogin/',homepage.as_view(),name='plogin'),
    #url('plogin/reg/',patientregister.as_view(),name='preg'),
    # url('plogin/update/',home2.views.add1,name="update"),
    url('',views.first,name="first"),
    # path('',homepage2.as_view(),name='home2'),

]