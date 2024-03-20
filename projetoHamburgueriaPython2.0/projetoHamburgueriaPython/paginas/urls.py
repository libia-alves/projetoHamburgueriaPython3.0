from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name="index"),
 
    path('cardapio/', views.cardapio,name="cardapio"),
   
    path('perfil/', views.perfil,name="perfil"),
    path('pratos/', views.pratos,name="pratos"),
    path('carrinho/', views.pratos,name="carrinho"),
    
    
]
