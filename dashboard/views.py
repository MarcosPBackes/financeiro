from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from carteiras.models import Fixa, Acao, Variavel, Entrada, Saida
from datetime import datetime
from django.db.models import Sum


class MinhaDash(View):
    def get(self, request):
        objetos= [Fixa, Variavel, Entrada, Saida]
        js = []

        for obj in objetos:
            entrada = obj.objects.all().filter(user=request.user)
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
                lista = sum([i.valor for i in entrada if i.data_e.month == mes and i.data_e.year == ano])
                labels.append(meses[mes - 1])
                data.append(lista)
                cont += 1
                data.append(js)
            json_entrada = {'data': data[::-1], 'labels': labels[::-1]}
        print(js)
        return JsonResponse(json_entrada)




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

