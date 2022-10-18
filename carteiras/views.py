from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import yfinance as yf
import investpy as inv

from .forms import AcaoForm, VariavelForm, FixaForm
from .models import Acao, Variavel, Fixa

import json
import pandas as pd

class Busca:
    def __int__(self, codigo):
        self.codigo = codigo
    def acao(self):
        cod = self.codigo
        res = yf.Ticker(cod)
        historico = res.history(period='2d')
        historico = historico.reset_index()
        historico.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'dividends', 'stock']
        historico['date'] = pd.to_datetime(historico['date'], errors='coerce')
        historico['date'] = historico['date'].dt.strftime('%m-%d-%Y')
        dts = historico.reset_index().to_json(orient='records', date_format='iso')
        cpt = [{'nome': res.info['longName'], 'tks': self.codigo.upper()}]
        cpp = json.dumps(cpt)
        cpp = json.loads(cpp)
        data = []
        data = json.loads(dts)
        return data, cpp
    #CPLE3.SA
def buscar(request):
    adicionar = VariavelForm(request.POST or None)
    search = request.GET.get('search')
    if search:
        tick = Busca()
        bs = search
        tick.codigo = bs.upper() + ".SA"
        res = tick.acao()
        acao = res[0]
        cpt = res[1]
        context = {
            'acao': acao,
            'cpt': cpt,
        }
        if request.POST:
            nome_a = res[1][0]['nome']
            tick_a = res[1][0]['tks']
            form = VariavelForm(request)
            return render(request, 'carteiras/acao_add.html', context)

        return render(request, 'carteiras/acao_list.html', context)
    else:
        return render(request, 'carteiras/acao_buscar.html')

def carteira(request):
    return render(request, 'carteiras/carteira.html')

def fixa_add(request):
    if request.method == 'POST':
        form = FixaForm(request.POST or None)

        if form.is_valid():
            fixa = form.save(commit=False)
            fixa.user = request.user
            fixa.save()
            return redirect('carteira')
    else:
        form = FixaForm()
        return render(request, 'carteiras/fixa_add.html', {'form': form})

def fixa_list(request):
    lista_f = Fixa.objects.all().order_by('-date_a').filter(user=request.user)
    paginator = Paginator(lista_f, 10)
    page = request.GET.get('page')
    lista = paginator.get_page(page)

    return render(request, 'carteiras/fixa_list.html', {'lista': lista})