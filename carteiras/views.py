from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import yfinance as yf
import investpy as inv

from .forms import VariavelForm, FixaForm, ContaeForm, ContasForm
from .models import Acao, Variavel, Fixa, Entrada, Saida

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
@login_required
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
@login_required
def carteira(request):
    return render(request, 'carteiras/carteira.html')
@login_required
def entrada_add(request):
    if request.method == 'POST':
        form = ContaeForm(request.POST or None)
        if form.is_valid():
            entrada = form.save(commit=False)
            entrada.user = request.user
            entrada.save()
            return redirect('carteira')
    else:
        form = ContaeForm()
        return render(request, 'carteiras/entrada_add.html', {'form': form})
@login_required
def entrada_list(request):
    lista_v = Entrada.objects.all().order_by('-data_a').filter(user=request.user)
    paginator = Paginator(lista_v, 10)
    page = request.GET.get('page')
    lista = paginator.get_page(page)
    return render(request, 'carteiras/entrada_list.html', {'lista': lista})
@login_required
def entrada_view(request, id):
    entrada = get_object_or_404(Entrada, pk=id)
    return render(request, 'carteiras/entrada_view.html', {'entrada': entrada})
@login_required
def entrada_edit(request, id):
    entrada = get_object_or_404(Entrada, pk=id)
    form = ContaeForm(instance=entrada)
    if(request.method == 'POST'):
        form = ContaeForm(request.POST, instance=entrada)
        if(form.is_valid()):
            entrada.save()
            return redirect('carteira')
        else:
            return render(request, 'carteiras/entrada_edit.html', {'form': form, 'entrada': entrada})
    else:
        return render(request, 'carteiras/entrada_edit.html', {'form': form, 'entrada': entrada})
@login_required
def entrada_delete(request, id):
    entrada = get_object_or_404(Entrada, pk=id)
    entrada.delete()
    messages.info(request, 'Deletado com sucesso!')
    return redirect('carteira')
@login_required
def saida_add(request):
    if request.method == 'POST':
        form = ContasForm(request.POST or None)
        if form.is_valid():
            saida = form.save(commit=False)
            saida.user = request.user
            saida.save()
            return redirect('carteira')
    else:
        form = ContasForm()
        return render(request, 'carteiras/saida_add.html', {'form': form})
@login_required
def saida_list(request):
    lista_v = Saida.objects.all().order_by('-data_a').filter(user=request.user)
    paginator = Paginator(lista_v, 10)
    page = request.GET.get('page')
    lista = paginator.get_page(page)
    return render(request, 'carteiras/saida_list.html', {'lista': lista})
@login_required
def saida_view(request, id):
    saida = get_object_or_404(Saida, pk=id)
    return render(request, 'carteiras/saida_view.html', {'saida': saida})
@login_required
def saida_edit(request, id):
    saida = get_object_or_404(Saida, pk=id)
    form = ContasForm(instance=saida)
    if(request.method == 'POST'):
        form = ContasForm(request.POST, instance=saida)
        if(form.is_valid()):
            saida.save()
            return redirect('carteira')
        else:
            return render(request, 'carteiras/saida_edit.html', {'form': form, 'saida': saida})
    else:
        return render(request, 'carteiras/saida_edit.html', {'form': form, 'saida': saida})
@login_required
def saida_delete(request, id):
    saida = get_object_or_404(Saida, pk=id)
    saida.delete()
    messages.info(request, 'Deletado com sucesso!')
    return redirect('carteira')
@login_required
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
@login_required
def variavel_list(request):
    lista_v = Variavel.objects.all().order_by('-data_a').filter(user=request.user)
    paginator = Paginator(lista_v, 10)
    page = request.GET.get('page')
    lista = paginator.get_page(page)
    return render(request, 'carteiras/variavel_list.html', {'lista': lista})
@login_required
def variavel_view(request, id):
    variavel = get_object_or_404(Variavel, pk=id)
    return render(request, 'carteiras/variavel_view.html', {'variavel': variavel})
@login_required
def variavel_edit(request, id):
    variavel = get_object_or_404(Variavel, pk=id)
    form = VariavelForm(instance=variavel)

    if(request.method == 'POST'):
        form = VariavelForm(request.POST, instance=variavel)
        if(form.is_valid()):
            variavel.save()
            return redirect('carteira')
        else:
            return render(request, 'carteiras/variavel_edit.html', {'form': form, 'variavel': variavel})
    else:
        return render(request, 'carteiras/variavel_edit.html', {'form': form, 'variavel': variavel})
@login_required
def variavel_delete(request, id):
    variavel = get_object_or_404(Variavel, pk=id)
    variavel.delete()
    messages.info(request, 'Investimento deletado com sucesso!')
    return redirect('carteira')
@login_required
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
@login_required
def fixa_list(request):
    lista_f = Fixa.objects.all().order_by('-data_a').filter(user=request.user)
    paginator = Paginator(lista_f, 10)
    page = request.GET.get('page')
    lista = paginator.get_page(page)
    return render(request, 'carteiras/fixa_list.html', {'lista': lista})
@login_required
def fixa_view(request, id):
    fixa = get_object_or_404(Fixa, pk=id)
    return render (request, 'carteiras/fixa_view.html', {'fixa': fixa})
@login_required
def fixa_edit(request, id):
    fixa = get_object_or_404(Fixa, pk=id)
    form = FixaForm(instance=fixa)

    if(request.method == 'POST'):
        form = FixaForm(request.POST, instance=fixa)
        if(form.is_valid()):
            fixa.save()
            return redirect('carteira')
        else:
            return render(request, 'carteiras/fixa_edit.html', {'form': form, 'fixa': fixa})
    else:
        return render(request, 'carteiras/fixa_edit.html', {'form': form, 'fixa': fixa})
@login_required
def fixa_delete(request, id):
    fixa = get_object_or_404(Fixa, pk=id)
    fixa.delete()
    messages.info(request, 'Investimento deletado com sucesso!')
    return redirect('carteira')