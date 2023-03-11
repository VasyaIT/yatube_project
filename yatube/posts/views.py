from django.shortcuts import render

from .models import Post


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def about(request):
    return render(request, 'posts/about.html')


def group_posts(request, slug):
    return render(request, 'posts/group_posts.html')
