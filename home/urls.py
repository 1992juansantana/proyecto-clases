from django.urls import path
from home import views


urlpatterns = [
    
    path("", views.index, name='index'),
    path("mi_template/", views.mi_template, name='mi_template'),
    path("ver_personas/", views.ver_personas, name='ver_persona'),
    path("crear_persona/", views.crear_persona, name='crear_persona'),
    path("curso", views.curso),
    path ("about/", views.nosotros, name='nosotros'),
     
    
    
]