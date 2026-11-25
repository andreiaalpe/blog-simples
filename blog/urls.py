from django.urls import path
from . import views

urlpatterns = [
    # Rota para página inicial
    path('', views.home, name='home'),

    # Rota para a página de contatos
    path('contacts/', views.contacts, name='contacts'),
    path('post/<int:id>/', views.post_detail,
         name='post_detail'),  # Página do post completo
    path('login/', views.login_view, name='login'),    # Login do usuário
]
