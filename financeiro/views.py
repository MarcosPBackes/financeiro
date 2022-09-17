from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import time
import json
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def acao_busca(request):
    url = "https://br.tradingview.com/screener/"
    option = Options()
    option.headless = True
    browser = webdriver.Chrome(options=option)
    browser.get(url)
    time.sleep(1)
    url_pego = browser.find_element(By.CLASS_NAME, "tv-screener__content-pane")
    html = url_pego.get_attribute('outerHTML')
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find(name='table')
    df = pd.read_html(str(table))[0].head(150)
    dfx = df[["CotaçãoSem resultados", "Preço", "Var %", "Var",
              "Technical Rating", "Vol", "Volume*Preço", "Valor de Mercado",
              "P/L", "EPS (12M)", "FUNCIONÁRIOS", "Setor"]]
    dfx.columns = ["nome", "fechamento", "variacao_p", "variacao_em_brl",
                   "indice_tecnico", "volume", "volume_vs_preco",
                   "valor_de_mercado", "relacao_preco_lucro",
                   "eps_12m", "funcionarios", "setor"]
    t_p = dfx[["nome", "fechamento", "variacao_p", "variacao_em_brl",
               "indice_tecnico", "volume", "volume_vs_preco",
               "valor_de_mercado", "relacao_preco_lucro",
               "eps_12m", "funcionarios", "setor"]]
    jotao = t_p.reset_index().to_json(orient='records')
    data = []
    data = json.loads(jotao)
    context = {'acao': data}
    return render(request, 'carteiras/acao_list.html', context)

def acao_search(request):
    url = "https://br.tradingview.com/screener/"
    option = Options()
    option.headless = True
    browser = webdriver.Chrome(options=option)
    browser.get(url)
    time.sleep(1)
    browser.find_element(By.CLASS_NAME,"tv-screener-table__search-input js-search-input").send_keys()
    pass

def carteiras(request):
    return render(request, 'carteiras/carteira.html')

def variavel_list(request):
    variavel_list = Variavel.objects.all().order_by('-created_at').filter(user=request.user)

    paginator = Paginator(variavel_list, 10)

    page = request.GET.get('page')

    variavel = paginator.get_page(page)

    return render(request, 'carteiras/variavel_list.html',
                  {'variavel': variavel})

def variavel_view(request, id):
   variavel = get_object_or_404(Variavel, pk=id)
   return render(request, 'carteiras/variavel_view.html',
                 {'variavel': variavel})

def variavel_add(request):
    if request.method == 'POST':
        form = VariavelForm(request.POST)

        if form.is_valid():
            variavel = form.save(commit=False)

            variavel.save()
            return redirect('variavel_list')
    else:
        form = VariavelForm()
        return render(request, 'carteiras/variavel_add.html',
                        {'form': form})

def variavel_edit(request, id):
    variavel = get_object_or_404(Variavel, pk=id)
    form = VariavelForm(instace=variavel)

    if(request.method == 'POST'):
        form = VariavelForm(request.POST, instance=variavel)
        if(form.is_valid()):
            variavel.save()
            return redirect('variavel_list')
        else:
            return render(request, 'carteiras/variavel_edit.html',
                          {'form':form, 'variavel':variavel})

def variavel_delete(request, id):
    variavel = get_object_or_404(Variavel, pk=id)
    variavel.delete()

    messages.info(request, 'Deletada com sucesso!')

    return redirect('variavel_list')


