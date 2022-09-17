from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import yfinance as yf
import investpy as inv


import json
import pandas as pd

class Busca:

    def __int__(self, codigo):
        self.codigo = codigo

    def acao(self):
        cod = self.codigo
        copel = yf.Ticker(cod)
        dados = copel.history(period="max")
        return dados


#CPLE3.SA
def buscar(request):
    search = request.GET.get('search')
    if search:
        tick = Busca()
        bs = search
        tick.codigo = bs.upper() + ".SA"
        res = tick.acao()
        data = []
        data = json.loads(res)
        return render(request, 'carteiras/acao_list.html',
                      {'acao':data})

    else:
        return render(request, 'carteiras/acao_list.html')
