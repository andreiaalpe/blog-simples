# blog/views/post_detail.py

from django.shortcuts import render, get_object_or_404
from ..models import Post

def post_detail(request, id):
    post = get_object_or_404(
        Post.objects.select_related('user'),
        id=id,
        is_active=True
    )

    return render(
        request, 
        'post_detail.html', 
        {'post': post}
    )