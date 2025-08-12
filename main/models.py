# seu_app/models.py
from django.db import models
from django.utils.text import slugify
import os
from django.utils import timezone
from django.contrib.auth.models import User

class CasoDeAjuda(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    imagem = models.ImageField(
        upload_to='casos/', 
        blank=True, 
        null=True,
        help_text="Dimensões recomendadas: 1024x768 pixels. Formatos: JPG, PNG. O arquivo deve ter menos de 2MB."
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Caso de Ajuda"
        verbose_name_plural = "Casos de Ajuda"
        ordering = ['-data_criacao']

    def __str__(self):
        return self.titulo

class Acao(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título da Ação")
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=255, verbose_name="Slug (URL Amigável)")
    descricao_breve = models.TextField(max_length=300, verbose_name="Descrição Breve")
    descricao_completa = models.TextField(verbose_name="Descrição Completa")
    imagem = models.ImageField(
        upload_to='acoes/', 
        blank=True, 
        null=True, 
        verbose_name="Imagem",
        help_text="Dimensões recomendadas: 800x600 pixels. Formatos: JPG, PNG."
    )
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

class Contato(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    observacoes = models.TextField(blank=True, verbose_name="Mensagem")
    data_recebimento = models.DateTimeField(auto_now_add=True)

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

    image = models.ImageField(
        upload_to='carousels/',
        help_text="Dimensões recomendadas: 1920x600 pixels. Formatos: JPG, PNG. Adequadas para banners grandes."
    )
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title or f"Imagem {self.pk} - {self.category}"

class Depoimento(models.Model):
    nome = models.CharField(max_length=100)
    texto = models.TextField()
    imagem = models.ImageField(
        upload_to='depoimentos/',
        blank=True,
        null=True,
        help_text="Adicione uma foto da pessoa. Dimensões recomendadas: 300x300 pixels. Formatos: JPG, PNG."
    )
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Depoimento"
        verbose_name_plural = "Depoimentos"
        ordering = ['-id']
        
    def __str__(self):
        return self.nome

class StaticImage(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text="Nome único para identificar a imagem no código (ex: 'hero_image', 'logo_footer').")
    image = models.ImageField(upload_to='static_images/', help_text="Carregue a imagem para este item. Dimensões e tipo variam de acordo com o uso.")
    description = models.CharField(max_length=200, blank=True, help_text="Breve descrição para o atributo 'alt' da imagem.")

    class Meta:
        verbose_name = "Imagem Estática"
        verbose_name_plural = "Imagens Estáticas"

    def __str__(self):
        return self.name

class Beneficiaria(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    nome_completo = models.CharField(max_length=255)
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    telefone = models.CharField(max_length=20, blank=True, verbose_name="Telefone de Contato")
    endereco = models.TextField(verbose_name="Endereço Completo")
    situacao_gravidez = models.CharField(max_length=100, help_text="Ex: '7º mês de gestação'", verbose_name="Situação da Gravidez")
    historico_medico = models.TextField(blank=True, verbose_name="Histórico Médico Relevante")
    necessidades = models.TextField(verbose_name="Necessidades Atuais (Enxoval, Alimentos, etc.)")
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Beneficiária"
        verbose_name_plural = "Beneficiárias"
        ordering = ['-data_cadastro']

    def __str__(self):
        return self.nome_completo

class Colaborador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Conta de Usuário")
    nome_completo = models.CharField(max_length=255, verbose_name="Nome Completo")
    cargo = models.CharField(max_length=100, help_text="Ex: 'Voluntário', 'Coordenador'", verbose_name="Cargo / Função")
    telefone = models.CharField(max_length=20, blank=True, verbose_name="Telefone de Contato")
    areas_interesse = models.TextField(verbose_name="Áreas de Interesse (Ex: Educação, Logística)", help_text="Selecione as áreas de atuação do colaborador.", blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"
        ordering = ['-data_cadastro']

    def __str__(self):
        return self.nome_completo

class BalancoFinanceiro(models.Model):
    """
    Modelo para gerenciar os documentos de balanço financeiro e transparência.
    """
    titulo = models.CharField(max_length=200, help_text="Ex: 'Relatório Anual de 2024'")
    descricao = models.TextField(help_text="Breve descrição do conteúdo do documento.")
    documento = models.FileField(upload_to='balancos/', help_text="Faça upload do arquivo PDF do balanço.")
    data_publicacao = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Balanço Financeiro"
        verbose_name_plural = "Balanços Financeiros"
        ordering = ['-data_publicacao']
    
    def __str__(self):
        return self.titulo
    
class PoliticaTransparencia(models.Model):
    """
    Modelo para gerenciar o documento da Política de Transparência.
    """
    titulo = models.CharField(max_length=200, help_text="Ex: 'Política de Transparência do Projeto Sarah'")
    documento = models.FileField(upload_to='politicas/', help_text="Faça upload do arquivo PDF da política.")
    data_publicacao = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Política de Transparência"
        verbose_name_plural = "Políticas de Transparência"
    
    def __str__(self):
        return self.titulo
