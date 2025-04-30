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