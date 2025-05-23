from django.db import models

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


class Depoimento(models.Model):
    imagem = models.ImageField(upload_to='depoimentos/', null=True, blank=True)
    titulo = models.CharField(max_length=255)
    texto = models.TextField()

    def __str__(self):
        return self.titulo

class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel/')
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):

        return self.title or "Carousel Image"
    
class Contato(models.Model):
    nome = models.CharField(max_length=200, null=True, default="Insira seu Nome")
    email = models.EmailField(null=True, default="Insira seu Email")
    telefone = models.CharField(max_length=20, null=True, default="Insira um telefone")
    observacoes = models.TextField(null=True, default='Sem observações')
    
    from django.db import models

class Missao(models.Model):
    titulo = models.CharField(max_length=200, null=True, default="Insira um Título")
    texto = models.TextField(null=True, default="Insira um texto")
    imagem = models.ImageField(upload_to='static/imagens', null=True)
    descricao_imagem = models.CharField(max_length=200, null=True, default="Insira a descrição da necessidade")
    
from django.db import models
from django.template.defaultfilters import slugify # Importa slugify para criar URLs amigáveis
import os # Para lidar com a exclusão de arquivos de imagem antigos

class Acao(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título da Ação")
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=255, verbose_name="Slug (URL Amigável)")
    descricao_breve = models.TextField(max_length=300, verbose_name="Descrição Breve")
    descricao_completa = models.TextField(verbose_name="Descrição Completa")
    imagem = models.ImageField(upload_to='acoes/', blank=True, null=True, verbose_name="Imagem")
    data_publicacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Publicação")
    ativa = models.BooleanField(default=True, verbose_name="Ação Ativa?") # Campo para ativar/desativar a ação

    class Meta:
        verbose_name = "Ação"
        verbose_name_plural = "Ações"
        ordering = ['-data_publicacao'] # Ordena as ações da mais recente para a mais antiga

    def save(self, *args, **kwargs):
        if not self.slug: # Gera o slug apenas se não houver um
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Exclui a imagem associada ao objeto quando o objeto é excluído
        if self.imagem:
            if os.path.isfile(self.imagem.path):
                os.remove(self.imagem.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.titulo