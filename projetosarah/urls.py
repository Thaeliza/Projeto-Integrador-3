# projetosarah/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Rota para o painel de administração do Django
    path('admin/', admin.site.urls),

    # Inclui as URLs do seu aplicativo 'main'
    path('', include('main.urls')),

    # Views de autenticação do Django para login e logout
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # A view de logout precisa ser configurada com o 'next_page'
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]

# Configuração para servir arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)