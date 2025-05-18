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