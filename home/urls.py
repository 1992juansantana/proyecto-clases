from django.urls import path
from home import views


urlpatterns = [
    
    path(" ", views.index),
    path("mi_template/", views.mi_template),
    path("ver_personas/", views.ver_personas),
    path("crear_persona/", views.crear_persona),
     
    
    
]