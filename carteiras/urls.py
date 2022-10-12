from django.urls import path, include
from . import views


urlpatterns = [
    path('acao_buscar/', views.buscar, name='acao_buscar'),
    path('acao_list/', views.buscar, name='acao_list'),
    path('carteira/', views.carteira, name='carteira'),
    path('fixa_add/', views.fixa_add, name='fixa_add'),
]