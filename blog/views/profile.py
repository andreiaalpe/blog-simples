# blog\views\profile.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from blog.forms import ProfileForm
from django.contrib.auth.views import PasswordChangeView as BasePasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


@login_required
def profile(request):

    # Usuário autenticado
    user = request.user

    # Postagens válidas do usuário, da mais recente para a mais antiga
    posts = user.posts.order_by('-created_at')

    return render(request, 'profile.html', {
        'user': user,
        'posts': posts,
    })


@login_required
def edit_profile(request):

    # Recebe os dados do usuário logado
    user = request.user

    # Recebe os dados do model do formulário
    form = ProfileForm(
        request.POST or None,
        request.FILES or None,
        instance=user
    )

    # Se o formulário foi enviado
    if request.method == 'POST':

        # Se os dados são válidos, salva no banco e exibe feedback no perfil
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('profile')

    # Mostra o formulário ainda não enviado e preenchido
    return render(
        request,
        'edit_profile.html',
        {'form': form}
    )

# view "especial" para mostrar mensagens de feedback na troca da senha
class PasswordChangeView(SuccessMessageMixin, BasePasswordChangeView):
    template_name = 'password/change.html'
    success_url = reverse_lazy('profile')
    success_message = 'Sua senha foi alterada com sucesso!'