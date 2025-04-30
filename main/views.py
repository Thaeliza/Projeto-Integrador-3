from django.shortcuts import render
from .models import CasoDeAjuda

def home(request):
    casos = CasoDeAjuda.objects.all()  # Busca todos os casos de ajuda do banco de dados
    return render(request, 'home.html', {'casos': casos})

from django.shortcuts import render
from .models import CasoDeAjuda

def home(request):
    casos = CasoDeAjuda.objects.all()
    return render(request, 'home.html', {'casos': casos})

def quem_somos(request):
    return render(request, 'quem_somos.html')

def como_ajudamos(request):
    return render(request, 'como_ajudamos.html')

def preciso_de_ajuda(request):
    return render(request, 'preciso_de_ajuda.html')

def como_ajudar(request):
    return render(request, 'como_ajudar.html')

def contato(request):
    return render(request, 'contato.html')