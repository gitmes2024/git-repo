from django.db import models

# Create your models here.

class tipoconf(models.Model):
     nombre=models.CharField(max_length=50)

def __str__(self):
    return self.nombre

class sala(models.Model):
     nombre=models.CharField(max_length=50)
     descripcion=models.TextField(max_length=100) 
     capacidad=models.IntegerField() 

def __str__(self):
    return self.nombre


class departamento(models.Model):
     nombre=models.CharField(max_length=50)
     descripcion=models.TextField(max_length=100) 
     telefono=models.CharField(max_length=10) 


def __str__(self):
    return self.nombre

class vconferencia(models.Model):
    tema=models.CharField(max_length=100)
    descripcion=models.TextField(max_length=300)   
    fechinicio=models.DateField()     
    horaInicio=models.TimeField()
    horaFinal=models.TimeField()
    tipoconf=models.ForeignKey(tipoconf,null=True,blank=True,on_delete=models.CASCADE)
    sala=models.ForeignKey(sala,null=True,blank=True,on_delete=models.CASCADE)
    departamento=models.ForeignKey(departamento,null=True,blank=True,on_delete=models.CASCADE)
    
def __str__(self):
    return self.tema