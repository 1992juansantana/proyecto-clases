from django.urls import path    
from avanzado import views

urlpatterns = [
    # version con vistas comunes 
    # path('motos/', views.ver_motos, name='ver_motos'),
    # path('motos/crear/', views.crear_moto, name='crear_moto'),
    # path('motos/editar/<int:id>', views.editar_moto, name='editar_moto'),
    # path('motos/eliminar/<int:id>', views.eliminar_moto, name='eliminar_moto')
    
    # version con clases basadas en vistas
    path('motos/', views.ListaMotos.as_view(), name='ver_motos'),
    path('motos/crear/', views.CrearMotos.as_view(), name='crear_moto'),
    path('motos/editar/<int:pk>', views.EditarMoto.as_view(), name='editar_moto'),
    path('motos/eliminar/<int:pk>', views.EliminarMoto.as_view(), name='eliminar_moto')
]
