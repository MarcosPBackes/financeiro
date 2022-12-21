from django.urls import path, include
from . import views

urlpatterns = [
    path('carteira_dashboard/', views.MinhaDash.as_view()),

]