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
    context = {
        # Você pode adicionar dados dinâmicos aqui no futuro, se precisar
    }
    return render(request, 'quem_somos.html', context) # Ajuste o caminho do template

def nossas_acoes(request):
    return render(request, 'nossas_acoes.html')

def transparencia(request):
    return render(request, 'transparencia.html')

def agenda_google_view(request):
    return render(request, 'agenda_google_view.html')

def doacao(request):
    return render(request, 'doacao.html')

def cadastro(request):
    return render(request, 'registration/login.html')

def preciso_de_ajuda(request):
    return render(request, 'preciso_de_ajuda.html')

def como_ajudar(request):
    return render(request, 'como_ajudar.html')

from django.shortcuts import render, redirect
from django.contrib import messages # Importe o módulo messages
from django.core.mail import send_mail
from django.conf import settings # Para acessar configurações do settings.py (email)

from .forms import ContatoForm # Importe seu formulário

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            # Lógica para enviar o e-mail
            try:
                send_mail(
                    f'CONTATO PELO SITE: {assunto} - De: {nome}', # Assunto do e-mail
                    f'Nome: {nome}\nEmail: {email}\nMensagem: {mensagem}', # Corpo do e-mail
                    settings.DEFAULT_FROM_EMAIL, # E-mail remetente configurado no settings.py
                    [settings.EMAIL_RECIPIENT], # Lista de e-mails para onde a mensagem será enviada
                    fail_silently=False,
                )
                messages.success(request, 'Sua mensagem foi enviada com sucesso! Em breve entraremos em contato.')
                return redirect('contato') # Redireciona para evitar reenvio do formulário
            except Exception as e:
                messages.error(request, f'Ocorreu um erro ao enviar sua mensagem. Tente novamente mais tarde. Erro: {e}')
    else:
        form = ContatoForm() # Cria um formulário vazio para requisições GET

    context = {
        'form': form,
    }
    return render(request, 'contato.html', context)

# seu_app/views.py
from django.shortcuts import render
from .models import Acao  # Importe seu modelo Acao

def lista_acoes(request):
    # Busca todas as ações do banco de dados, ordenadas pela data de publicação (mais recentes primeiro)
    acoes = Acao.objects.all().order_by('-data_publicacao') 
    context = {
        'acoes': acoes,  # 'acoes' é a variável que o template vai iterar
    }
    return render(request, 'seu_app/nossas_acoes.html', context)

