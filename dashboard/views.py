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
        data_f = pd.DataFrame(js, columns=['jan', 'fev', 'mar', 'abr', 'mai',
                                           'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'])
        data_f.index = ['fixa', 'variavel', 'entrada', 'saida']
        json_r = data_f.to_json()
        return (json_r)
def home_dash(request):
    dados = MinhaDash.get(request)
    df = pd.read_json(dados)
    df = df.T
    sum_inv = sum(df['fixa']) + sum(df['variavel'])
    sum_entrada = sum(df['entrada'])
    sum_saida = sum(df['saida'])
    context = {
        'investimento': sum_inv,
        'entrada': sum_entrada,
        'saida': sum_saida
    }
    return render(request, 'dashboard/carteira_dashboard.html', context)
