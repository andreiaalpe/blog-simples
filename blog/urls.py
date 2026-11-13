from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                   # ← Rota da página inicial que já existe
    path('contacts/', views.contacts, name='contacts'),  # ← Adicionamos a rota para `contacts` aqui
]