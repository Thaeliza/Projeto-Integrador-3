from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import Contato
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contato, Beneficiaria, Colaborador



class BeneficiariaForm(forms.ModelForm):
    class Meta:
        model = Beneficiaria
        fields = ['nome_completo', 'data_nascimento', 'telefone', 'endereco', 'situacao_gravidez']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'situacao_gravidez': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome_completo', 'cargo', 'telefone']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ContatoForm(forms.ModelForm):
    """
    Formulário de contato que interage com o modelo Contato,
    com um campo adicional para o assunto do e-mail.
    """
    assunto = forms.CharField(
        label="Assunto",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Qual o motivo do seu contato?'}),
        required=True
    )
    
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone', 'observacoes']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemplo.com'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira um telefone (opcional)'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Escreva sua mensagem aqui...'}),
        }

# Formulário de Autenticação Customizado
class CustomAuthenticationForm(AuthenticationForm):
    """
    Estiliza o formulário de login padrão do Django com classes do Bootstrap.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})


