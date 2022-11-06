from django.urls import path    
from avanzado import views

urlpatterns = [
    path('motos/', views.ver_motos, name='ver_motos'),
    path('motos/crear/', views.crear_moto, name='crear_moto')
]
