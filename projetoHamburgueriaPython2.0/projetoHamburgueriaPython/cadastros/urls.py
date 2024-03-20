from django.urls import path
from .views import  ProdutoCreate,CarrinhoCreate
from .views import ProdutoUpdate, CarrinhoUpdate, ProdutoDelete, CarrinhoDelete
from .views import ProdutoListView, CarrinhoListView



urlpatterns = [
  
    path('cadastrar/produtos/',ProdutoCreate.as_view(),name="cadastrar-produtos"),
    
    
    path('cadastrar/carrinhos/',CarrinhoCreate.as_view(),name="cadastrar-carrinhos"),



    
    
     #=== UPDATE 
    path('editar/produtos/<int:pk>/',ProdutoUpdate.as_view(),name="editar-produtos"), 
      path('editar/carrinhos/<int:pk>/',CarrinhoUpdate.as_view(),name="editar-carrinhos"), 
   # path('editar/Produto/<int:pk>/',AtividadeUpdate.as_view(),name="editar-Produto"), 
    
    #=== LISTAR
   # path('listar/Produto/>',CampoListView.as_view(),name="listar-Produto"),   
    path('listar/produtos/',ProdutoListView.as_view(),name="listar-produtos"),
    path('listar/carrinhos/',CarrinhoListView.as_view(),name="listar-carrinhos"),
    
    
    path('excluir/produtos/<int:pk>/',ProdutoDelete.as_view(), name='excluir-produtos'),
    path('excluir/carrinhos/<int:pk>/',CarrinhoDelete.as_view(), name='excluir-carrinhos'),

    ]