# core\urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Adiciona as URLS de 'blog' ao projeto
    path('', include('blog.urls')),

    # Logout do usuário
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
