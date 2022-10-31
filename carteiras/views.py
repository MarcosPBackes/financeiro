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
            acao = Acao(tks=tick_a, nome=nome_a)
            acao.save()
            return redirect('variavel_add')

        return render(request, 'carteiras/acao_list.html', context)
    else:
        return render(request, 'carteiras/acao_buscar.html')

def carteira(request):
    return render(request, 'carteiras/carteira.html')

def variavel_add(request):
    if request.method == 'POST':
        form = VariavelForm(request.POST or None)

        if form.is_valid():
            variavel = form.save(commit=False)
            variavel.user = request.user
            variavel.save()
            return redirect('carteira')
    else:
        form = VariavelForm()
        return render(request, 'carteiras/variavel_add.html', {'form': form})

def variavel_list(request):
    lista_v = Variavel.objects.all().order_by('-date_a').filter(user=request.user)
    paginator = Paginator(lista_v, 10)
    page = request.GET.get('page')
    lista = paginator.get_page(page)
    return render(request, 'carteiras/variavel_list.html', {'lista': lista})
def variavel_view(request, id):
    variavel = get_object_or_404(Variavel, pk=id)
    return render (request, 'carteiras/variavel_view.html', {'variavel': variavel})
def variavel_edit(request, id):
    variavel = get_object_or_404(Variavel, pk=id)
    form = VariavelForm(instance=variavel)

    if(request.method == 'POST'):
        form = VariavelForm(request.POST, instance=variavel)
        if(form.is_valid()):
            variavel.save()
            return redirect('carteira')
        else:
            return render(request, 'carteiras/variavel_edit.html', {'form':form, 'variavel':variavel})

    else:
        return render(request, 'carteiras/variavel_edit.html', {'form': form, 'variavel':variavel})
def variavel_delete(request, id):
    variavel = get_object_or_404(Variavel, pk=id)
    variavel.delete()
    messages.info(request, 'Investimento deletado com sucesso!')
    return redirect('carteira')
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

def fixa_view(request, id):
    fixa = get_object_or_404(Fixa, pk=id)
    return render (request, 'carteiras/fixa_view.html', {'fixa': fixa})

def fixa_edit(request, id):
    fixa = get_object_or_404(Fixa, pk=id)
    form = FixaForm(instance=fixa)

    if(request.method == 'POST'):
        form = FixaForm(request.POST, instance=fixa)
        if(form.is_valid()):
            fixa.save()
            return redirect('carteira')
        else:
            return render(request, 'carteiras/fixa_edit.html', {'form':form, 'fixa':fixa})

    else:
        return render(request, 'carteiras/fixa_edit.html', {'form': form, 'fixa': fixa})

def fixa_delete(request, id):
    fixa = get_object_or_404(Fixa, pk=id)
    fixa.delete()
    messages.info(request, 'Investimento deletado com sucesso!')

    return redirect('carteira')