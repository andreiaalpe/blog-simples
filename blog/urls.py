# blog\urls.py

from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

urlpatterns = [
    # Rota para página inicial
    path('', views.home, name='home'),

    # Rota para a página de contatos
    path('contacts/', views.contacts, name='contacts'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # Página do post completo
    
    # Login do usuário
    path('login/', views.login_view, name='login'),
    
    # Perfil do usuário logado
    path('profile/', views.profile, name='profile'),
    
    # Editar perfil do usuário logado
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    
    # Troca da senha
    path(
        'profile/password/',
        PasswordChangeView.as_view(),
        name='password_change'
    ),
]
