from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from carteiras.models import Fixa, Acao, Variavel, Entrada, Saida
from datetime import datetime
from django.db.models import Sum

def minha_dashboard(request):
    entrada = Entrada.objects.all().filter(user=request.user)
    saida = Saida.objects.all().filter(user=request.user)
    fixa = Fixa.objects.all().filter(user=request.user)
    variavel = Variavel.objects.all().filter(user=request.user)
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
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

        list_e = sum([i.valor for i in entrada if i.data_e.month == mes and i.data_e.year == ano])
        list_s = sum([i.valor for i in saida if i.data_e.month == mes and i.data_e.year == ano])
        list_f = sum([i.valor for i in fixa if i.data_e.month == mes and i.data_e.year == ano])
        list_v = sum([i.valor for i in variavel if i.data_e.month == mes and i.data_e.year == ano])
        labels.append(meses[mes - 1])
        data.append(list_e, list_s)
        cont += 1


    data_json = {'data': data[::-1], 'labels': labels[::-1]}
    print(data_json['data'])
    res = sum(data_json['data'])

    print(res)

    return JsonResponse(data_json)


def renda_variavel():
    pass
def renda_fixa():
    pass
def tipos_investimento():
    pass
def recebimentos():
    pass
def pagamentos():
    pass

