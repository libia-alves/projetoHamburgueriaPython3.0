from django.db import models


class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50, choices=[('bebida', 'Bebida'), ('hamburguer', 'Hambúrguer'), ('sorvete', 'Sorvete'), ('porcao', 'Porção')])

    def __str__(self):
        return"{} - {}({})".format(self.nome,self.preco,self.categoria)

class Carrinhos(models.Model):
   qtde=models.IntegerField(max_length=50,verbose_name='qtde')
   categoria = models.CharField(max_length=50, choices=[('bebida', 'Bebida'), ('hamburguer', 'Hambúrguer'), ('sorvete', 'Sorvete'), ('porcao', 'Porção')]) 
  
   form=models.CharField(max_length=50, choices=[('cartao', 'Cartão de Crédito'), ('cartao', 'Cartão de Débito'), ('pix', 'Pix')]) 
   produto=models.ForeignKey(Produtos,on_delete=models.PROTECT)
   
   def __str__(self):
        return"{} - {}({})".format(self.qtde,self.categoria,self.form,self.produto)