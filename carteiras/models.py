from django.db import models
from django.contrib.auth import get_user_model

class Acao(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    codigo = models.CharField(max_length=6)
    nome = models.CharField(max_length=128)
    data_compra = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.nome
    

class Fixa(models.Model):
    pass



class Variavel(models.Model):
    acao = models.ForeignKey(Acao, on_delete=models.PROTECT)
    preco_medio = models.DecimalField(max_digits=11, decimal_places=2)
    quantidade = models.IntegerField()
    user =  models.ForeignKey(get_user_model(), on_delete=models.PROTECT)