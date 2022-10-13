from django.urls import path
from home import views


urlpatterns = [
    
    
    path("mi_template/", views.mi_template),
    path("ver_personas/", views.ver_personas),
    path("crear_persona/>str:nombre>/<str:apellido>/", views.crear_persona),
     
    
    
]