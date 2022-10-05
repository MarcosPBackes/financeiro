from django.http import HttpResponse
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
        return copel
    #CPLE3.SA
def buscar(request):
    search = request.GET.get('search')
    if search:
        tick = Busca()
        bs = search
        tick.codigo = bs.upper() + ".SA"
        res = tick.acao()
        historico = res.history(period='30d')
        historico = historico.reset_index()
        historico.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'dividends', 'stock']
        historico['date'] = pd.to_datetime(historico['date'], errors='coerce')
        historico['date'] = historico['date'].dt.strftime('%m-%d-%Y')
        dts = historico.reset_index().to_json(orient='records', date_format='iso')
        cpt = [{'nome': res.info['longName']}, {'tks': bs.upper()}]
        cpt = json.dumps(cpt)
        cpt = json.loads(cpt)
        data = []
        data = json.loads(dts)
        context = {'acao': data,
                   'cpt': cpt,
                   }
        return render(request, 'carteiras/acao_list.html', context)
    else:
        return render(request, 'carteiras/acao_buscar.html')

def carteira(request):
    return render(request, 'carteiras/carteira.html')