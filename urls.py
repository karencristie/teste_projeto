"""
URL configuration for gestor_demandas project.

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
# gestor_demandas/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView # <--- Importe o RedirectView

urlpatterns = [
    # Adicione esta linha: quando alguém acessar a raiz, redirecione para /login/
    path('', RedirectView.as_view(url='/login/', permanent=False)),
    
    path('admin/', admin.site.urls),
    path('tarefas/', include('tarefas.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='tarefas/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]