from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'sobre/home.html')


import yfinance as yf



class Busca:

    def __int__(self, codigo):
        self.codigo = codigo

    def acao(self):
        cod = self.codigo
        copel = yf.Ticker(cod)
        dados = copel.history(period="max")

        print(dados)
        return dados

def acao_busca():
    tick = Busca()
    tick.codigo = "CPLE3.SA"
    tick.acao()
    return tick.acao()

