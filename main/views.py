from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContatoForm
from main.models import CarouselImage
from .models import CasoDeAjuda, Acao, Depoimento, Beneficiaria, Colaborador, BalancoFinanceiro, PoliticaTransparencia
from .forms import ContatoForm, BeneficiariaForm, ColaboradorForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test


def transparencia(request):
    """
    Renderiza a página de transparência com a lista de balanços e a política.
    """
    balancos = BalancoFinanceiro.objects.all()
    politica = PoliticaTransparencia.objects.first() # Pega a política mais recente
    context = {
        'balancos': balancos,
        'politica': politica,
    }
    return render(request, 'transparencia.html', context)


@login_required
@user_passes_test(lambda u: u.is_staff)
def relatorio_usuarios(request):
    """
    Renderiza a página de relatório de usuários, acessível apenas por administradores.
    """
    beneficiarias = Beneficiaria.objects.all()
    colaboradores = Colaborador.objects.all()
    context = {
        'beneficiarias': beneficiarias,
        'colaboradores': colaboradores,
    }
    return render(request, 'relatorio_usuarios.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def cadastro_beneficiaria(request):
    """
    Renderiza a página de cadastro de beneficiária, acessível apenas por administradores.
    """
    if request.method == 'POST':
        form = BeneficiariaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Beneficiária cadastrada com sucesso!')
            return redirect('home')
    else:
        form = BeneficiariaForm()
    
    return render(request, 'cadastro_beneficiaria.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def cadastro_colaborador(request):
    """
    Renderiza a página de cadastro de colaborador, acessível apenas por administradores.
    """
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador cadastrado com sucesso!')
            return redirect('home')
    else:
        form = ColaboradorForm()
    
    return render(request, 'cadastro_colaborador.html', {'form': form})

def home(request):
    """
    Renderiza a página inicial com os casos de ajuda e depoimentos.
    """
    casos = CasoDeAjuda.objects.all()
    depoimentos = Depoimento.objects.filter(ativo=True)
    home1_images = CarouselImage.objects.filter(category='home1')
    home2_images = CarouselImage.objects.filter(category='home2')
    
    context = {
        'casos': casos,
        'depoimentos': depoimentos,
        'carousel_home1_images': home1_images,
        'carousel_home2_images': home2_images,
    }
    return render(request, 'home.html', context)

def quem_somos(request):
    return render(request, 'quem_somos.html')

def nossas_acoes(request):
    acoes = Acao.objects.filter(ativa=True)
    return render(request, 'nossas_acoes.html', {'acoes': acoes})

def detalhe_acao(request, slug):
    """
    Renderiza a página de detalhes de uma ação específica.
    """
    acao = get_object_or_404(Acao, slug=slug, ativa=True)
    return render(request, 'detalhe_acao.html', {'acao': acao})


def doacao(request):
    return render(request, 'doacao.html')

def preciso_de_ajuda(request):
    return render(request, 'preciso_de_ajuda.html')

def como_ajudar(request):
    return render(request, 'como_ajudar.html')

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            # Salva os dados do formulário no banco de dados
            contato_instance = form.save(commit=False)
            contato_instance.observacoes = form.cleaned_data['observacoes']
            contato_instance.save()
            
            # Prepara o e-mail
            nome = form.cleaned_data['nome']
            email_remetente = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['observacoes']

            try:
                send_mail(
                    f'CONTATO PELO SITE: {assunto} - De: {nome}',
                    f'Nome: {nome}\nEmail: {email_remetente}\nMensagem: {mensagem}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.EMAIL_RECIPIENT],
                    fail_silently=False,
                )
                messages.success(request, 'Sua mensagem foi enviada com sucesso! Em breve entraremos em contato.')
                return redirect('contato')
            except Exception as e:
                print(f"Erro ao enviar e-mail de contato: {e}") 
                messages.error(request, 'Ocorreu um erro ao enviar sua mensagem. Tente novamente mais tarde.')
        else:
            messages.error(request, 'Por favor, corrija os erros no formulário.')
    else:
        form = ContatoForm()

    return render(request, 'contato.html', {'form': form})


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sua conta foi criada com sucesso! Agora você pode fazer login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/registro.html', {'form': form})
