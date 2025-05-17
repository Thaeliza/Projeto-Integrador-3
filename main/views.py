from django.shortcuts import render,redirect
from .models import CasoDeAjuda,CarouselImage
from .forms import ContatoForm 

def home(request):
    casos = CasoDeAjuda.objects.all()
    carousel_images = CarouselImage.objects.filter(is_active=True)
    return render(request, 'home.html', {'casos': casos,'carousel_images': carousel_images})
    

def quem_somos(request):
    return render(request, 'quem_somos.html')

def como_ajudamos(request):
    return render(request, 'como_ajudamos.html')

def preciso_de_ajuda(request):
    return render(request, 'preciso_de_ajuda.html')

def como_ajudar(request):
    return render(request, 'como_ajudar.html')

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContatoForm()

    return render(request, 'contato.html', {'form': form})