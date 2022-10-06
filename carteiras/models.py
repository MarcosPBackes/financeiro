from django.db import models
from django.contrib.auth import get_user_model

class Acao(models.Model):
    tks = models.CharField(max_length=5)
    nome = models.CharField(max_length=155)
    date_a = models.DateField(auto_now=True)

class Fixa(models.Model):
    valor_inv = models.DecimalField(max_digits=11, decimal_places=2)
    rendimento = models.DecimalField(max_digits=5, decimal_places=2)
    tempo = [
        ('DIA', 'Diario'),
        ('MES', 'Mensal'),
        ('TRI', 'Trimestral'),
        ('SEM', 'Semestral'),
        ('ANO', 'Anual'),
    ]



class Variavel(models.Model):
    acao = models.ForeignKey(Acao, on_delete=models.PROTECT)
    preco_medio = models.DecimalField(max_digits=11, decimal_places=2)
    quantidade = models.IntegerField()
    valor_pago = models.DecimalField(max_digits=11, decimal_places=2)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

