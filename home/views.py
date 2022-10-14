from contextvars import Context
from email.headerregistry import MessageIDHeader
from django.http import HttpResponse
from datetime import datetime
from django.template import loader, Context, Template
from django.shortcuts import render
import random

from home.models import Persona

def mi_template(request):
    
    cargar_archivo = open(r'C:\Users\juan_\OneDrive\Escritorio\proyecto-clases\templates\mi_template.html')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    
    contexto = Context()
    
    template_renderizado = template.render(contexto)  
      
    return HttpResponse(template_renderizado)  

def crear_persona(request):
    
    personas1 = Persona(nombre="Lionel", apellido="Messi", edad=35)
    personas2 = Persona(nombre="Antonella", apellido="Roccuzzo", edad=34)
    personas3 = Persona(nombre="Thiago", apellido="Messi", edad=9)
    
    
    
    
    personas1.save()
    personas2.save()
    personas3.save()
    
    return render(request, "home/crear_persona.html", {"personas": personas1})
    


def ver_personas(request):
    
    
    personas = Persona.objects.all()
    
    return render(request, "home/ver_personas.html", {"personas": personas})
    


# def curso(request,nombre,apellido,edad):
    
    
#     persona1 = Persona(nombre=nombre , apellido=apellido, edad=edad)
    
#     return render(request, "curso.html", {"persona1":persona1})
    

   

      
   
    
    