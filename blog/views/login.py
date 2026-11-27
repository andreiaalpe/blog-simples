# blog/views/login.py

from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme

def login_view(request):
    # Se o form não foi enviado
    if request.method != 'POST':
        return redirect('home')

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(
        request,
        username=username,
        password=password
    )
    next_url = request.POST.get('next') or reverse('home')

    if not url_has_allowed_host_and_scheme(
        next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure()
    ):
        next_url = reverse('home')

    if user is not None:
        auth_login(request, user)
        messages.success(
            request,
            'Login realizado com sucesso!'
        )
    else:
        messages.error(
            request,
            'Usuário ou senha inválidos!'
        )

    return redirect(next_url)