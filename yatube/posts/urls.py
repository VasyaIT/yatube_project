from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('contact_done/', views.contact_done, name='contact_done'),
    path('about/author/', views.About.as_view(), name='about'),
    path('about/tech/', views.Tech.as_view(), name='tech'),
    path('posts/<int:post_id>/comment/', views.add_comment, name='add_comment'),

]
