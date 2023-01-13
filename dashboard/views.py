from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from carteiras.models import Fixa, Acao, Variavel, Entrada, Saida
from datetime import datetime
from django.db.models import Sum

import json
import numpy as np
import pandas as pd

class MinhaDash():
    def get(request):
        objetos = [Fixa, Variavel, Entrada, Saida]
        js = []
        ultimos = []
        for obj in objetos:
            entrada = obj.objects.all().filter(user=request.user)
            meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul',
                     'ago', 'set', 'out', 'nov', 'dez']
            data = []
            labels = []
            cont = 0
            mes = datetime.now().month + 1
            ano = datetime.now().year
            for i in range(12):
                mes -= 1
                if mes == 0:
                    mes = 12
                    ano -= 1
                lista = sum([i.valor for i in entrada if i.data_e.month == mes and i.data_e.year == ano])
                labels.append(meses[mes - 1])
                data.append(lista)
                cont += 1
            js.append(data)
        for obj in objetos:
            cinco_ultimos = obj.objects.all().order_by('-id')[:3]
            ultimos.append(cinco_ultimos)
            #print(cinco_ultimos)
        data_f = pd.DataFrame(js, columns=['jan', 'fev', 'mar', 'abr', 'mai',
                                           'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'])
        data_f.index = ['fixa', 'variavel', 'entrada', 'saida']
        json_r = data_f.to_json()
        return json_r, ultimos

def home_dash(request):
    dados = MinhaDash.get(request)
    df = pd.read_json(dados[0])
    ultimos = dados[1]
    df = df.T
    sum_inv = sum(df['fixa']) + sum(df['variavel'])
    sum_entrada = sum(df['entrada'])
    sum_saida = sum(df['saida'])
    ult_fixa = ultimos[0]
    ult_variavel = ultimos[1]
    ult_entrada = ultimos[2]
    ult_saida = ultimos[3]
    context = {
        'sum_investimento': sum_inv,
        'sum_entrada': sum_entrada,
        'sum_saida': sum_saida,
        'ult_fixa': ult_fixa,
        'ult_variavel': ult_variavel,
        'ult_entrada': ult_entrada,
        'ult_saida': ult_saida,
    }
    return render(request, 'dashboard/carteira_dashboard.html', context)
