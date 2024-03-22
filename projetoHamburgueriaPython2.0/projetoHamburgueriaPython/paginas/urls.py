from django.urls import path
from . import views


urlpatterns = [ 
               
    path('perfil/', views.perfil,name="perfil"),
    path('restrito/', views.restrito,name="restrito"),
    path('', views.home,name="index"),

 
    path('cardapio/', views.cardapio,name="cardapio"),
   

    path('pratos/', views.pratos,name="pratos"),
    path('carrinho/', views.pratos,name="carrinho"),
    
    
]
