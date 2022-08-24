from django.shortcuts import render
from hospital.models import Pacient,Doctor,TypeAppointment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.timezone import now
from django.core import serializers 


# Create your views here.
@api_view(['GET', 'POST','PUT','DELETE'])
def view_pacient(request,pk=None):
    response={'error':False,'msg':'OK','data':None}
    data=request.data
    if request.method == 'GET':
        pacients=Pacient.objects.filter(deleted_at =None).values()
        return Response({'error':False ,'data': list(pacients)})

    if request.method=='POST':
        try:
            if  not Pacient.objects.filter( dni=data['dni']).exists():
                created = Pacient.objects.create(name=data['name'],lastname=data['lastname'],dni=data['dni'])
                created.save()
            else:
                response={'error':True,'msg':'Existing DNI','data':data['dni']}
        except Exception as e:
           return Response({'error':True,'msg':'error','data':str(e)})   
        return Response( response)

    if request.method=='PUT' and pk!= None:
        try:
            pacient=Pacient.objects.get(pk=pk)
            pacient.name=data['name']
            pacient.lastname=data['lastname']
            pacient.dni=data['dni']
            pacient.updated_at=now()
            pacient.save()
        except Exception as e:
           return Response({'error':True,'msg':'error','data':str(e)})   
        return Response(response)
        
    if request.method=='DELETE' and pk != None:
        try:
            pacient=Pacient.objects.get(pk=pk)
            pacient.deleted_at=now()
            pacient.save()
        except Exception as e:
           return Response({'error':True,'msg':'error','data':str(e)})   
        return Response(response)
    

@api_view(['GET', 'POST','PUT','DELETE'])
def view_doctor(request,pk=None):
    data=request.data
    if request.method == 'GET':
        doctors=Doctor.objects.filter(deleted_at =None).values()
        return Response({'error':False ,'data': list(doctors)})

    if request.method=='POST':
        try:
            if  not Pacient.objects.filter( dni=data['dni']).exists():
                created = Doctor.objects.create(name=data['name'],lastname=data['lastname'],dni=data['dni'])
                created.save()
            else:
                response={'error':True,'msg':'Existing DNI','data':data['dni']}
        except Exception as e:
           return Response({'error':True,'msg':'error','data':str(e)},)   
        return Response( response)

    if request.method=='PUT' and pk!= None:
        try:
            doctor=Doctor.objects.get(pk=pk)
            doctor.name=data['name']
            doctor.lastname=data['lastname']
            doctor.dni=data['dni']
            doctor.updated_at=now()
            doctor.save()
        except Exception as e:
           return Response({'error':True,'msg':'error','data':str(e)})   
        return Response(response)

    if request.method=='DELETE' and pk != None:
        try:
            doctor=Doctor.objects.get(pk=pk)
            doctor.deleted_at=now()
            doctor.save()
        except Exception as e:
           return Response({'error':True,'msg':'error','data':str(e)})   
        return Response(response)



@api_view(['GET', 'POST','PUT','DELETE'])
def view_TypeAppointment(request,pk=None):
    data=request.data
    if request.method == 'GET':
        typeAppointment=TypeAppointment.objects.filter(deleted_at =None).values()
        return Response({'error':False ,'data': list(typeAppointment)})

    if request.method=='POST':
        try:
            created = TypeAppointment.objects.create(description=data['description'],)
            created.save()
        except Exception as e:
           return Response({'error':True,'msg':'error','data':str(e)},)   
        return Response( {'error':False,'msg':'OK','data':str(created)})

    if request.method=='PUT' and pk!= None:
        try:
            typeAppointment=TypeAppointment.objects.get(pk=pk)
            typeAppointment.description=data['description']
            typeAppointment.updated_at=now()
            typeAppointment.save()
        except Exception as e:
           return Response({'error':True,'msg':'error','data':str(e)})   
        return Response( {'error':False,'msg':'OK','data':str(typeAppointment)})

    if request.method=='DELETE' and pk != None:
        try:
            typeAppointment=TypeAppointment.objects.get(pk=pk)
            typeAppointment.deleted_at=now()
            typeAppointment.save()
        except Exception as e:
           return Response({'error':True,'msg':'error','data':str(e)})   
        return Response( {'error':False,'msg':'OK','data':str(typeAppointment)})





@api_view(['GET', 'POST','PUT','DELETE'])
def view_Appointment(request,pk=None):
    data=request.data
    if request.method == 'GET':
        typeAppointment=TypeAppointment.objects.filter(deleted_at =None).values()
        return Response({'error':False ,'data': list(typeAppointment)})

    if request.method=='POST':
        try:
            created = TypeAppointment.objects.create(description=data['description'],)
            created.save()
        except Exception as e:
           return Response({'error':True,'msg':'error','data':str(e)},)   
        return Response( {'error':False,'msg':'OK','data':str(created)})

    if request.method=='PUT' and pk!= None:
        try:
            typeAppointment=TypeAppointment.objects.get(pk=pk)
            typeAppointment.description=data['description']
            typeAppointment.updated_at=now()
            typeAppointment.save()
        except Exception as e:
           return Response({'error':True,'msg':'error','data':str(e)})   
        return Response( {'error':False,'msg':'OK','data':str(typeAppointment)})

    if request.method=='DELETE' and pk != None:
        try:
            typeAppointment=TypeAppointment.objects.get(pk=pk)
            typeAppointment.deleted_at=now()
            typeAppointment.save()
        except Exception as e:
           return Response({'error':True,'msg':'error','data':str(e)})   
        return Response( {'error':False,'msg':'OK','data':str(typeAppointment)})


