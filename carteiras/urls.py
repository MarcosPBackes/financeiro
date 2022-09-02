from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.carteiras, name='carteiras'),
    path('<int:id>', views.variavel_view, name='variavel_view'),
    path('variavel_add/', views.variavel_add, name='variavel_add'),
    path('variavel_edit/<int:id>/', views.variavel_edit, name='variavel_edit'),
    path('variavel_delete/<int:id>/', views.variavel_delete, name='variavel_delete'),
    path('acao_list/', views.acao_busca, name='acao_busca'),
]