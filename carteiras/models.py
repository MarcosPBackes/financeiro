from django.db import models
from django.contrib.auth import get_user_model

tempo_porcentagem = [
        ('DIA', 'Diario'),
        ('MES', 'Mensal'),
        ('TRI', 'Trimestral'),
        ('SEM', 'Semestral'),
        ('ANO', 'Anual'),
    ]

tipo_renda_fixa = [
    ('TED', 'Tesouro Direto'),
    ('CBD', 'CBD'),
    ('LCI', ' LCI/LCA'),
    ('DBT', 'Debêntures'),
    ('LDC', 'Letras de Câmbio'),
    ('CRI', 'CRI/CRA'),
    ('POP', 'Poupança'),
    ('OTR', 'Outro')
]
class Fixa(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    data_a = models.DateField(auto_now=True)
    valor = models.DecimalField(max_digits=11, decimal_places=2)
    rendimento = models.DecimalField(max_digits=5, decimal_places=2)
    tempo = models.CharField(max_length=3, choices=tempo_porcentagem)
    tipo = models.CharField(max_length=3, choices=tipo_renda_fixa)
    descricao_tipo = models.CharField(max_length=155)
    data_e = models.DateField(null=False, blank=False)

class Acao(models.Model):
    tks = models.CharField(max_length=10)
    nome = models.CharField(max_length=155)
    data_a = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome
class Variavel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    data_a = models.DateField(auto_now=True)
    data_e = models.DateField(null=False, blank=False)
    acao = models.ForeignKey(Acao, on_delete=models.PROTECT, blank=False, null=False)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=11, decimal_places=2)

class Entrada(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    descricao = models.CharField(max_length=155, verbose_name='Descrição')
    faturado = models.BooleanField(default=False)
    valor = models.DecimalField(max_digits=11, decimal_places=2)
    data_a = models.DateField(auto_now=True)
    data_e = models.DateField(null=False, blank=False, verbose_name='Data de vencimento')
class Saida(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    descricao = models.CharField(max_length=155, verbose_name='Descrição')
    faturado = models.BooleanField(default=False)
    valor = models.DecimalField(max_digits=11, decimal_places=2)
    data_a = models.DateField(auto_now=True)
    data_e = models.DateField(null=False, blank=False, verbose_name='Data de vencimento')
