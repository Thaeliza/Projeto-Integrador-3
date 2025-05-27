        
# seu_app/models.py
from django.db import models
from django.utils.text import slugify
import os # Para a função delete da Acao
# seu_app/models.py
from django.db import models
from django.utils import timezone # <--- ADICIONE ESTE IMPORT NO TOPO DO ARQUIVO


class CasoDeAjuda(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='casos/', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Caso de Ajuda"
        verbose_name_plural = "Casos de Ajuda"
# Modelo de Ação

class Acao(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título da Ação")
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=255, verbose_name="Slug (URL Amigável)")
    descricao_breve = models.TextField(max_length=300, verbose_name="Descrição Breve")
    descricao_completa = models.TextField(verbose_name="Descrição Completa")
    imagem = models.ImageField(upload_to='acoes/', blank=True, null=True, verbose_name="Imagem")
    data_publicacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Publicação")
    ativa = models.BooleanField(default=True, verbose_name="Ação Ativa?")

    class Meta:
        verbose_name = "Ação"
        verbose_name_plural = "Ações"
        ordering = ['-data_publicacao']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.imagem:
            if os.path.isfile(self.imagem.path):
                os.remove(self.imagem.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.titulo




# Modelo de Contato
class Contato(models.Model):
    nome = models.CharField(max_length=200, null=True, default="Insira seu Nome")
    email = models.EmailField(null=True, default="Insira seu Email")
    telefone = models.CharField(max_length=20, null=True, default="Insira um telefone")
    observacoes = models.TextField(null=True, default='Sem observações')
    # Mude esta linha:
    data_recebimento = models.DateTimeField(auto_now_add=True)
 # <--- ADICIONE default=timezone.now
    # OU, se você quiser apenas um padrão para a migração inicial sem que ele seja um padrão para novos objetos
    # data_recebimento = models.DateTimeField(auto_now_add=True, verbose_name="Data de Recebimento")
    # E ao rodar makemigrations, escolha a opção 1 e use 'timezone.now' como o padrão.

    class Meta:
        verbose_name = "Contato Recebido"
        verbose_name_plural = "Contatos Recebidos"
        ordering = ['-data_recebimento']

    def __str__(self):
        return f"Contato de {self.nome} ({self.email})"

class CarouselImage(models.Model):
    CATEGORY_CHOICES = [
        ('base', 'Carrossel Base'),
        ('home1', 'Carrossel Home 1'),
        ('home2', 'Carrossel Home 2'),
    ]

    image = models.ImageField(upload_to='carousels/')
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title or f"Imagem {self.pk} - {self.category}"
    

class Depoimento(models.Model):
    nome = models.CharField(max_length=100)  # substitui 'author'
    texto = models.TextField()               # substitui 'text'
    ativo = models.BooleanField(default=True)  # substitui 'is_active'

    def __str__(self):
        return self.nome



