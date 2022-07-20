from django.db import models

class Carteira(models.Model):
    pass

class Variavel(models.Model):
    pass

class Fixa(models.Model):
    pass

class Acao(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    codigo = models.CharField(max_length=6)
    nome = models.CharField(max_length=128)
    data_compra = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 