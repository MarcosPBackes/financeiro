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
        res = yf.Ticker(cod)
        historico = res.history(period='5d')
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

def buscar():
    search = "petr4"
    adicionar = True
    if search:
        tick = Busca()
        bs = search
        tick.codigo = bs.upper() + ".SA"
        res = tick.acao()
        data = res[0]
        acao_nome = res[1][0]['nome']
        acao_tick = res[1][0]['tks']
        #print(data)
        print(type(acao_nome))
        print(acao_tick)
#buscar()

def fixa_list(request):
    lista_f = Fixa.objects.all().order_by('-date_a').filter(user=request.user)

    paginator = Paginator(lista_f, 10)
    page = request.GET.get('page')
    lista = paginator.get_page(page)
    print(lista)
#fixa_list('marcos')