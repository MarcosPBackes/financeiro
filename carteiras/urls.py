from django.urls import path, include
from . import views


urlpatterns = [
    path('acao_buscar/', views.buscar, name='acao_buscar'),
    path('acao_list/', views.buscar, name='acao_list'),

]