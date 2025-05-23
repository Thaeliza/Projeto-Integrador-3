from django import forms
from .models import Contato

        
class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone', 'observacoes']  # Use 'observacoes' aqui
        
        


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