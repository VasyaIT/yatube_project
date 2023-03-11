from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ContactForm
from .models import Post
from django.core.paginator import Paginator


def index(request):
    posts = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(posts, 10)

    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')

    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)
    # Отдаем в словаре контекста
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def about(request):
    return render(request, 'posts/about.html')


def group_posts(request, slug):
    return render(request, 'posts/group_posts.html')


class Contact(CreateView):
    form_class = ContactForm
    template_name = 'posts/contact.html'
    success_url = reverse_lazy('contact_done')


def contact_done(request):
    return render(request, 'posts/contact_done.html')
