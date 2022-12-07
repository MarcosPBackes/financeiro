from django.urls import path, include
from . import views

urlpatterns = [
    path('carteira_dashboard/', views.minha_dashboard, name='carteira_dasgboard'),

]