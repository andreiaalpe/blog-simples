from django.shortcuts import render
from blog.models import Post

def home(request):

    # Obtém todos os `post` usando filtros e ordenamento
    posts = Post.objects.filter(
        is_active=True
    ).order_by('-created_at')       # Ordenados pela data mais recente

    return render(
        request,
        'home.html',
        {
            'posts': posts,                  # Todos os post filtrados
            'total_posts': posts.count(),    # Quantos post recebemos
            'show_aside': False,             # Oculta a <aside> da página
        }
    )