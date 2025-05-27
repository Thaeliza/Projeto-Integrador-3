# projetosarah/urls.py (o urls.py PRINCIPAL do seu projeto)

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # Importe as views de autenticação do Django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]

