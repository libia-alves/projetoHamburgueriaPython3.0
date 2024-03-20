from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import  ListView

from django.shortcuts import render, redirect
from .models import Produtos, Carrinhos

from django.urls import reverse_lazy

class ProdutoCreate(CreateView):
    
    model=Produtos
    fields=['nome','preco', 'categoria']
    template_name='cadastros/form.html'
    success_url=reverse_lazy('index')
    
    
class CarrinhoCreate(CreateView):
    model=Carrinhos
    fields=['qtde','categoria', 'Preco','form','produto']
    template_name='cadastros/form.html'
    success_url=reverse_lazy('index')
    
    
 

#===== Função de atualização Update

class ProdutoUpdate(UpdateView):
    model=Produtos
    fields=['nome','descricao', 'valor']
    template_name='cadastros/form.html'
    success_url=reverse_lazy('index')
    
class CarrinhoUpdate(UpdateView):
    model=Carrinhos
    fields=['qtde','categoria', 'Preco', 'form', 'produto']
    template_name='cadastros/form.html'
    success_url=reverse_lazy('index')
    


class ProdutoDelete(DeleteView):
      model=Produtos
      template_name='cadastros/form_excluir.html'
      success_url=reverse_lazy('index')   
      
class CarrinhoDelete(DeleteView):
      model=Carrinhos
      template_name='cadastros/form_excluir.html'
      success_url=reverse_lazy('index')   
 

class ProdutoListView(ListView):
    model=Produtos
    template_name='cadastros/listar/campo.html'
    
class CarrinhoListView(ListView):
    model=Carrinhos
    template_name='cadastros/listar/campo.html'



