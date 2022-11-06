from contextvars import Context
from email.headerregistry import MessageIDHeader
from django.http import HttpResponse
from datetime import datetime
from django.template import loader, Context, Template
from django.shortcuts import render, redirect
import random
from home.forms import PersonaFormulario, BusquedaFormulario

from home.models import Persona

def mi_template(request):
    
    cargar_archivo = open(r'C:\Users\juan_\OneDrive\Escritorio\proyecto-clases\home\templates\home\mi_template.html')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    
    contexto = Context()
    
    template_renderizado = template.render(contexto)  
      
    return HttpResponse(template_renderizado)  

def crear_persona(request):
    
    if request.method =='POST':
        
        formulario = PersonaFormulario(request.POST)
      
        if formulario.is_valid():
            data = formulario.cleaned_data
    
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']

        
            persona = Persona(nombre=nombre, apellido=apellido, edad=edad)
            persona.save()
    
            return redirect('ver_personas')
    
    formulario = PersonaFormulario()
   
    return render(request, 'home/crear_persona.html', {'formulario': formulario})
    


def ver_personas(request):
    
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        personas = Persona.objects.filter(nombre__incontains=nombre)
    else:
        personas = Persona.objects.all()
    
    formulario = BusquedaFormulario()
    
    return render(request, "home/ver_personas.html", {"personas": personas, "formulario": formulario})


def index(request):
    
    return render(request, "home/index.html")
    


def curso(request):
    
    return render(request, "home/curso.html")
    

   

      
   
    
    