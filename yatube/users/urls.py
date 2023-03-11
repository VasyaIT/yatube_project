from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.urls import path


urlpatterns = [
    path('logout/', LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('password_change/', views.password_change, name='password_change'),
    path('password_change/done/', views.password_change_done, name='password_change_done'),
]
