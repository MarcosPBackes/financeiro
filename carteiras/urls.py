from django.urls import path, include
from . import views

urlpatterns = [
    path('acao_buscar/', views.buscar, name='acao_buscar'),
    path('acao_list/', views.buscar, name='acao_list'),
    path('entrada_list/', views.entrada_list, name='entrada_list'),
    path('entrada_add/', views.entrada_add, name='entrada_add'),
    path('entrada_view/<int:id>/', views.entrada_view, name='entrada_view'),
    path('entrada_edit/<int:id>/', views.entrada_edit, name='entrade_edit'),
    path('entrada_delete/<int:id>/', views.entrada_delete, name='entrada_delete'),
    path('saida_list/', views.saida_list, name='saida_list'),
    path('saida_add/', views.saida_add, name='saida_add'),
    path('saida_view/<int:id>/', views.saida_view, name='saida_view'),
    path('saida_edit/<int:id>/', views.saida_edit, name='saida_edit'),
    path('saida_delete/<int:id>', views.saida_delete, name='saida_delete'),
    path('variavel_list/', views.variavel_list, name='variavel_list'),
    path('variavel_add/', views.variavel_add, name='variavel_add'),
    path('variavel_view/<int:id>/', views.variavel_view, name='variavel_view'),
    path('variavel_edit/<int:id>/', views.variavel_edit, name='variavel_edit'),
    path('variavel_delete/<int:id>/', views.variavel_delete, name='variavel_delete'),
    path('carteira/', views.carteira, name='carteira'),
    path('fixa_add/', views.fixa_add, name='fixa_add'),
    path('fixa_list/', views.fixa_list,  name='fixa_list'),
    path('fixa_view/<int:id>/', views.fixa_view, name='fixa_view'),
    path('fixa_edit/<int:id>/', views.fixa_edit, name='fixa_edit'),
    path('fixa_delete/<int:id>/', views.fixa_delete, name='fixa_delete'),
]
