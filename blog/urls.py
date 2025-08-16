# blog/urls.py
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    
    path('', views.blog_list, name='blog_list'),
    path("blogs/<slug:slug>/detail/", views.blog_detail, name="blog_detail"),
    path('blogs/create/', views.blog_create, name='blog_add'),
    path('blogs/<int:pk>/update/', views.blog_update, name='blog_update'),
    path('blogs/<int:pk>/delete/', views.blog_delete, name='blog_delete'),
]


