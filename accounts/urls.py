from django.urls import path
from . import views

app_name = 'accounts'  # Required for namespacing

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', views.user_list, name='user_list'),
]
