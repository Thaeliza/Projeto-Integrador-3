


# seu_app/admin.py
from django.contrib import admin
from .models import Acao, Contato, CarouselImage, Depoimento,CasoDeAjuda # Importe todos os seus modelos
from django.utils.text import slugify # Importe slugify

admin.site.register(CasoDeAjuda)


class AcaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao', 'ativa', 'slug')
    search_fields = ('titulo', 'descricao_breve', 'descricao_completa')
    list_filter = ('ativa', 'data_publicacao')
    prepopulated_fields = {'slug': ('titulo',)}
    list_editable = ('ativa',)
    fieldsets = (
        (None, {
            'fields': ('titulo', 'slug', 'ativa', 'imagem')
        }),
        ('Conteúdo', {
            'fields': ('descricao_breve', 'descricao_completa')
        }),
        ('Detalhes Adicionais', {
            'fields': ('data_publicacao',),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('data_publicacao',)

admin.site.register(Acao, AcaoAdmin)

# Admin para Contato
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'data_recebimento') # Adicione data_recebimento se tiver no modelo
    search_fields = ('nome', 'email', 'observacoes')
    list_filter = ('data_recebimento',) # Se tiver este campo
    readonly_fields = ('data_recebimento',) # Se tiver este campo

admin.site.register(Contato, ContatoAdmin)



class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)


admin.site.register(CarouselImage, CarouselImageAdmin)

# Admin para Depoimento
class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ('author', 'is_active', 'text')
  
@admin.register(Depoimento)
class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'texto')  # campos corretos
    list_filter = ('ativo',)
    list_editable = ('ativo',)