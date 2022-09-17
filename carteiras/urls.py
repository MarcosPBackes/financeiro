from django.urls import path, include
from . import views


urlpatterns = [
    path('acao_list/', views.buscar, name='acao_list'),

]