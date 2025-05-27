# seu_app/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Contato # Importe seu modelo Contato

# Formulário de Contato (ModelForm para salvar dados e campos extras para e-mail)
from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(
        label="Seu Nome",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome completo'})
    )
    email = forms.EmailField(
        label="Seu E-mail",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemplo.com'})
    )
    assunto = forms.CharField(
        label="Assunto",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Qual o motivo do seu contato?'})
    )
    mensagem = forms.CharField(
        label="Sua Mensagem",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Escreva sua mensagem aqui...'}),
        help_text="Máximo de 500 caracteres."
    )
    class Meta:
        model = Contato
        # Campos do modelo que serão exibidos no formulário (assunto e mensagem são campos extras)
        fields = ['nome', 'email', 'telefone']
        widgets = { # Estiliza os campos do modelo com Bootstrap
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemplo.com'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira um telefone'}),
            # Se você quisesse usar 'observacoes' no form, adicionaria aqui
            # 'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }

# Formulário de Autenticação Customizado (para estilizar o login com Bootstrap)
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})