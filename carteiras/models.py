from django.db import models
from django.contrib.auth import get_user_model

tempo_porcentagem = [
        ('DIA', 'Diario'),
        ('MES', 'Mensal'),
        ('TRI', 'Trimestral'),
        ('SEM', 'Semestral'),
        ('ANO', 'Anual'),
    ]
class Fixa(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    date_a = models.DateField(auto_now=True)
    valor_inv = models.DecimalField(max_digits=11, decimal_places=2)
    rendimento = models.DecimalField(max_digits=5, decimal_places=2)
    tempo = models.CharField(max_length=3, choices=tempo_porcentagem)
    data_inv = models.DateTimeField()
class Acao(models.Model):
    tks = models.CharField(max_length=5)
    nome = models.CharField(max_length=155)
    date_a = models.DateField(auto_now=True)



class Variavel(models.Model):
    acao = models.ForeignKey(Acao, on_delete=models.PROTECT)
    preco_medio = models.DecimalField(max_digits=11, decimal_places=2)
    quantidade = models.IntegerField()
    valor_pago = models.DecimalField(max_digits=11, decimal_places=2)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

