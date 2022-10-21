from django.urls import path, include
from . import views


urlpatterns = [
    path('acao_buscar/', views.buscar, name='acao_buscar'),
    path('acao_list/', views.buscar, name='acao_list'),
    path('carteira/', views.carteira, name='carteira'),
    path('fixa_add/', views.fixa_add, name='fixa_add'),
    path('fixa_list/', views.fixa_list,  name='fixa_list'),
    path('fixa_view/<int:id>', views.fixa_view, name='fixa_view'),
    path('fixa_edit/<int:id>/', views.fixa_edit,name='fixa_edit'),
    path('fixa_delete/<int:id>', views.fixa_delete, name='fixa_delete'),
]