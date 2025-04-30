from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quem-somos/', views.quem_somos, name='quem_somos'),
    path('como-ajudamos/', views.como_ajudamos, name='como_ajudamos'),
    path('preciso-de-ajuda/', views.preciso_de_ajuda, name='preciso_de_ajuda'),
    path('como-ajudar/', views.como_ajudar, name='como_ajudar'),
    path('contato/', views.contato, name='contato'),
]