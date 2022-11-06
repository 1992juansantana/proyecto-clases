from django.shortcuts import render, redirect
from avanzado.forms import MotoFormulario
from avanzado.models import Moto


# Create your views here.

def ver_motos(request):
    
    motos = Moto.objects.all()
    
    return render(request, 'avanzado/ver_motos.html', {'motos': motos})

def crear_moto(request):
    
    if request.method == 'POST':
        formulario = MotoFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            
            moto = Moto(
                marca=datos['marca'], 
                modelo=datos['modelo'],
                edad=datos['edad']
            )
            moto.save()
            return redirect('ver_motos')
        return render(request, 'avanzado/crear_motos.html', {'formulario': formulario})
    
    formulario = MotoFormulario()
    return render(request, 'avanzado/crear_motos.html', {'formulario': formulario})