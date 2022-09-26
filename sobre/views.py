from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'sobre/home.html')

import json
import pandas as pd
import yfinance as yf



class Busca:

    def __int__(self, codigo):
        self.codigo = codigo

    def acao(self):
        cod = self.codigo
        copel = yf.Ticker(cod)
        #dados = copel.history(period="max")

        return copel

def buscar():
    search = "petr4"
    if search:
        tick = Busca()
        bs = search
        tick.codigo = bs.upper() + ".SA"
        res = tick.acao()
        historico = res.history(period='2d')
        historico = historico.reset_index()
        historico.columns = ["date", "open", "high", "low", "close", "volume", "dividends", "stock"]
        djs = historico.reset_index().to_json(orient='records', date_format='iso')
        data = []
        data = json.loads(djs)
        #print(data.date, data.open)
        print(data)
        print(djs)

    else:
        pass
#buscar()