from django.shortcuts import render, redirect
from avanzado.forms import MotoFormulario

from avanzado.models import Moto

from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

def ver_motos(request):
    
    motos = Moto.objects.all()
    
    return render(request, 'avanzado/ver_motos.html', {'motos': motos})

@login_required # decorador para que no pueda logear
def crear_moto(request):
    
    if request.method == 'POST':
        formulario = MotoFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            
            moto = Moto(
                marca=datos['marca'], 
                modelo=datos['modelo'],
                anio=datos['anio']
            )
            moto.save()
            return redirect('ver_motos')
        
    
    formulario = MotoFormulario()
    return render(request, 'avanzado/crear_moto.html', {'formulario': formulario})


def editar_moto(request, id):
    
    moto = Moto.objects.get(id=id)
    
    if request.method == 'POST':
        formulario = MotoFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            
            moto.marca = datos['marca']
            moto.modelo = datos['modelo']
            moto.anio = datos['anio']

            moto.save()
            
            return redirect('ver_motos')
        else:
            return render(request, 'avanzado/editar_moto.html', {'formulario': formulario})
            
    
    formulario = MotoFormulario(
        initial={
            'marca': moto.marca,
            'modelo': moto.modelo,
            'anio': moto.anio,
           
        }
    )
    
    return render(request, 'avanzado/editar_moto.html', {'formulario': formulario, 'moto': moto})


def eliminar_moto(request, id):
    moto = Moto.objects.get(id=id)
    moto.delete()
    return redirect('ver_motos')



class ListaMotos(ListView):
    model = Moto
    template_name = 'avanzado/ver_motos_cbv.html'
    
class CrearMotos(CreateView):
    model= Moto
    success_url = '/avanzado/motos/'
    template_name = 'avanzado/crear_moto_cbv.html'
    fields = ['marca', 'modelo', 'anio']    
    
class EditarMoto(LoginRequiredMixin, UpdateView):
    model= Moto
    success_url = '/avanzado/motos/'
    template_name = 'avanzado/editar_moto_cbv.html'
    fields = ['marca', 'modelo', 'anio'] 
    
class EliminarMoto(LoginRequiredMixin, DeleteView):
    model= Moto
    success_url = '/avanzado/motos/'
    template_name = 'avanzado/eliminar_moto_cbv.html'
    




