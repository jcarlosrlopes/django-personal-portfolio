from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    all_posts = Post.objects.order_by('publish_date')
    return render(request, 'blog/home.html', { 'posts': all_posts })

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', { 'post': post })
