from django.shortcuts import render
from .models import CasoDeAjuda
from main.models import CarouselImage  # ou o nome da sua app


from django.shortcuts import render
from .models import CarouselImage

def home(request):
    home1_images = CarouselImage.objects.filter(category='home1')
    home2_images = CarouselImage.objects.filter(category='home2')
    return render(request, 'home.html', {
        'carousel_home1_images': home1_images,
        'carousel_home2_images': home2_images,
    })



def base_context(request):
    carousel_base_images = CarouselImage.objects.filter(category='base')
    return {'carousel_base_images': carousel_base_images}

def home(request):
    casos = CasoDeAjuda.objects.all()
    return render(request, 'home.html', {'casos': casos})

def quem_somos(request):
    return render(request, 'quem_somos.html')

def nossas_acoes(request):
    return render(request, 'nossas_acoes.html')

def transparencia(request):
    return render(request, 'transparencia.html')


def doacao(request):
    return render(request, 'doacao.html')

def cadastro(request):
    return render(request, 'registration/login.html')

def preciso_de_ajuda(request):
    return render(request, 'preciso_de_ajuda.html')

def como_ajudar(request):
    return render(request, 'como_ajudar.html')

def contato(request):
    return render(request, 'contato.html')