from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import ContactForm, CommentForm
from .models import Post, Group, Comment
from django.core.paginator import Paginator


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)

    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')

    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts,
        'page_obj': page_obj
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = Group.objects.get(slug=slug)
    posts = group.group_posts.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    user = User.objects.get(username=username)
    posts = user.posts.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'user': user,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = CommentForm(request.POST or None)
    comments = post.comments.all()
    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    return render(request, 'posts/post_detail.html', context)


class Contact(CreateView):
    form_class = ContactForm
    template_name = 'posts/contact.html'
    success_url = reverse_lazy('contact_done')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Contact, self).form_valid(form)

# def contact(request):
#     form = ContactForm(request.POST)
#     if form.is_valid():
#         contacts = form.save(commit=False)
#         contacts.user = request.user
#         contacts.save()
#         return redirect('contact_done')
#     form = ContactForm()
#     return render(request, 'posts/contact.html', {'form': form})


def contact_done(request):
    return render(request, 'posts/contact_done.html')


class About(TemplateView):
    template_name = 'posts/about.html'


class Tech(TemplateView):
    template_name = 'posts/tech.html'


@login_required
def add_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('post_detail', post_id=post_id)
