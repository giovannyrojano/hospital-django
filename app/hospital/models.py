from django.db import models
from django.utils.timezone import now
# Create your models here.

class Pacient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name',max_length=100, null=False)
    lastname = models.CharField('Lastname', max_length=100, null=False)
    dni = models.CharField('Dni', max_length=100,null=False)
    created_at = models.DateTimeField(default=now, editable=True, null=False)
    updated_at=models.DateTimeField(default=now, editable=True ,null=False)
    deleted_at=models.DateTimeField(blank=True, null=True)

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name',max_length=100, null=False)
    lastname = models.CharField('Lastname', max_length=100,null=False)
    dni = models.CharField('Dni', max_length=100,null=False)
    created_at = models.DateTimeField(default=now, editable=True, null=False)
    updated_at=models.DateTimeField(default=now, editable=True ,null=False)
    deleted_at=models.DateTimeField(blank=True, null=True)


class TypeAppointment(models.Model):
    id = models.AutoField(primary_key=True)
    description =models.TextField('Description',blank=False, null=False)
    created_at = models.DateTimeField(default=now, editable=True, null=False)
    updated_at=models.DateTimeField(default=now, editable=True ,null=False)
    deleted_at=models.DateTimeField(blank=True, null=True)
    

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    doctor =models.ForeignKey('doctor', models.DO_NOTHING)
    pacient = models.ForeignKey('pacient', models.DO_NOTHING)
    type=models.ForeignKey('TypeAppointment', models.DO_NOTHING)
    date = models.CharField('Dni', max_length=100,blank=False, null=False)
    created_at = models.DateTimeField(default=now, editable=True, null=False)
    updated_at=models.DateTimeField(default=now, editable=True ,null=False)
    deleted_at=models.DateTimeField(blank=True, null=True)