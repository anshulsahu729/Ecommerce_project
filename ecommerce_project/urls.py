"""
URL configuration for ecommerce_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls', namespace='store')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('newsletter/', include('newsletter.urls', namespace='newsletter')),
    # path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('auth/', include('accounts.urls', namespace='accounts')),
    # path('api/', include('crm_api.urls', namespace='crm_api')),
]
