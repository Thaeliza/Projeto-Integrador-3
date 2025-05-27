# seu_app/urls.py (o urls.py DENTRO do seu aplicativo)

from django.urls import path
from . import views # Aqui sim, 'from . import views' está correto

urlpatterns = [
    path('quem-somos/', views.quem_somos, name='quem_somos'),
    path('', views.home, name='home'),
    path('nossas_acoes/', views.nossas_acoes, name='nossas_acoes'),
    path('transparencia/', views.transparencia, name='transparencia'),
    path('preciso-de-ajuda/', views.preciso_de_ajuda, name='preciso_de_ajuda'),
    path('como-ajudar/', views.como_ajudar, name='como_ajudar'),
    path('registration/login/', views.cadastro, name='cadastro'),
    path('contato/', views.contato, name='contato'),
    path('doacao/', views.doacao, name='doacao'), # Se 'doacao' for uma URL separada
    # path('cadastro/', views.cadastro, name='cadastro'), # URL para a view de cadastro
]