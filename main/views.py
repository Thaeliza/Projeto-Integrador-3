from django.shortcuts import render,redirect,get_object_or_404
from .models import CasoDeAjuda,CarouselImage,Depoimento
from .forms import ContatoForm 
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect


def home(request):
    casos = CasoDeAjuda.objects.all()
    carousel_images = CarouselImage.objects.filter(is_active=True)
    depoimentos = Depoimento.objects.all()    
    return render(request, 'home.html', {'casos': casos, 'carousel_images': carousel_images, 'depoimentos': depoimentos})
    
def quem_somos(request):
    return render(request, 'quem_somos.html')

def como_ajudamos(request):
    return render(request, 'como_ajudamos.html')

def preciso_de_ajuda(request):
    return render(request, 'preciso_de_ajuda.html')

def como_ajudar(request):
    return render(request, 'como_ajudar.html')

def doacao(request):
    return render(request, 'doacao.html')

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContatoForm()

    return render(request, 'contato.html', {'form': form})


def doacao(request):
    return render(request, 'doacao.html')

def cadastro(request):

  if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            cadastro(request, user)
            return HttpResponseRedirect('/admin')  # Redireciona para a página de administração
        else:
            return render(request, 'cadastro.html', {'error': 'Usuário ou senha inválidos'})
  else:
        return render(request, 'cadastro.html')
    

# def lista_acoes(request):
#     # Pega todas as ações ativas, ordenadas pela data de publicação (mais recente primeiro)
#     acoes = Acao.objects.filter(ativa=True).order_by('-data_publicacao')
#     context = {
#         'acoes': acoes
#     }
#     return render(request, 'meuapp/lista_acoes.html', context) # Renderiza seu template com as ações

# def detalhe_acao(request, slug):
#     # Pega uma ação específica pelo slug, ou retorna 404 se não encontrar
#     acao = get_object_or_404(Acao, slug=slug, ativa=True)
#     context = {
#         'acao': acao
#     }
#     return render(request, 'meuapp/detalhe_acao.html', context)