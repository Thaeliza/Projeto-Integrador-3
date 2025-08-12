from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quem-somos/', views.quem_somos, name='quem_somos'),
    path('nossas-acoes/', views.nossas_acoes, name='nossas_acoes'),
    path('nossas-acoes/<slug:slug>/', views.detalhe_acao, name='detalhe_acao'),
    path('como-ajudar/', views.como_ajudar, name='como_ajudar'),
    path('doacao/', views.doacao, name='doacao'),
    path('transparencia/', views.transparencia, name='transparencia'),
    path('contato/', views.contato, name='contato'),
    path('registro/', views.registro, name='registro'),
    path('cadastro-beneficiaria/', views.cadastro_beneficiaria, name='cadastro_beneficiaria'),
    path('cadastro-colaborador/', views.cadastro_colaborador, name='cadastro_colaborador'),
    path('relatorio-usuarios/', views.relatorio_usuarios, name='relatorio_usuarios'),
]