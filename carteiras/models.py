from django.db import models
from django.contrib.auth import get_user_model

class Acao(models.Model):
    pass
    

class Fixa(models.Model):
    pass



class Variavel(models.Model):
    acao = models.ForeignKey(Acao, on_delete=models.PROTECT)
    preco_medio = models.DecimalField(max_digits=11, decimal_places=2)
    quantidade = models.IntegerField()
    user =  models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

