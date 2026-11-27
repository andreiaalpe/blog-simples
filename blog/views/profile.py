from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def profile(request):

    # Usuário autenticado
    user = request.user

    # Postagens válidas do usuário, da mais recente para a mais antiga
    posts = user.posts.order_by('-created_at')

    return render(
        request,
        'profile.html',
        {
            'user': user,
            'posts': posts,

        }
    )
