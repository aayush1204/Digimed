
from django.contrib import admin
from django.urls import path,include
from . import views
from home2.views import medreccall,add1
#from django.contrib.staticfiles.urls.static import static

urlpatterns = [
    # path('',views.home1,name="home1"),
    
    path('fileview/',views.readingfile,name="fileview"),
    path('update/',views.add1,name="update"),
    path('plogin/update',views.add1,name="update"),
    #path('plogin/update/',views.add1,name="update"),
    path('update/bookappointment/conbook/<int:p>',views.conbook,name="conbook"),
    path('update/bookappointment/',views.appbook,name="bookappointment"),
    path('bookappointment/',views.appbook,name="bookappointment"),
    path('conbook/<int:p>',views.conbook,name="conbook"),
    path('plogin/log/bookappointment',views.appbook,name="bookappointment"),
    path('records/',medreccall.as_view(),name='records'),
    #path('log/appoint/',views.home3,name="appoint"),
    path('plogin/log/update',views.add1,name="update"),
    path('plogin/log/appoint',views.home3,name="appoint"),
]
