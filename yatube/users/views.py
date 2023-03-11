from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignUpForm

User = get_user_model()


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


def password_change(requests):
    return render(requests, 'users/password_change_form.html')


def password_change_done(request):
    return render(request, 'users/password_change_done.html')
