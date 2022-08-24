

from django.urls import path ,include
from . import  views

urlpatterns = [ 
    path('pacient', views.view_pacient),   
    path('pacient/<pk>', views.view_pacient),   

    path('doctor', views.view_doctor),   
    path('doctor/<pk>', views.view_doctor),   
    
    path('TypeAppointment', views.view_TypeAppointment),   
    path('TypeAppointment/<pk>', views.view_TypeAppointment),   


]