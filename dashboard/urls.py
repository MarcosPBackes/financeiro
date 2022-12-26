from django.urls import path, include
from . import views

urlpatterns = [
    path('carteira_dashboard/', views.home_dash, name='dash')

]