from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import yfinance as yf
import investpy as inv

from .forms import AcaoForm, VariavelForm
from .models import Acao, Variavel

import json
import pandas as pd

class Busca:
    def __int__(self, codigo):
        self.codigo = codigo
    def acao(self):
        cod = self.codigo
        res = yf.Ticker(cod)
        historico = res.history(period='5d')
        company_name = res.info['longName']
        historico = historico.reset_index()
        historico.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'dividends', 'stock']
        historico['date'] = pd.to_datetime(historico['date'], errors='coerce')
        historico['date'] = historico['date'].dt.strftime('%m-%d-%Y')
        dts = historico.reset_index().to_json(orient='records', date_format='iso')
        cpt = [{'nome': res.info['longName'], 'tks': self.codigo.upper()}]
        cpp = json.dumps(cpt)
        return dts, cpp
    #CPLE3.SA
def buscar(request):
    search = request.GET.get('search')
    adicionar = request.GET.get('adicionar')

    if search:
        tick = Busca()
        bs = search
        tick.codigo = bs.upper() + ".SA"
        res = tick.acao()
        dat = res[0][]
        return render(request, 'carteiras/acao_list.html', context)



    else:
        return render(request, 'carteiras/acao_buscar.html')

def carteira(request):
    return render(request, 'carteiras/carteira.html')