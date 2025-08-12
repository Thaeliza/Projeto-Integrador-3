# seu_app/admin.py
from django.contrib import admin
from .models import Acao, Contato, CarouselImage, Depoimento, CasoDeAjuda, StaticImage, Beneficiaria, Colaborador, BalancoFinanceiro, PoliticaTransparencia

# Registrando os novos modelos
@admin.register(Beneficiaria)
class BeneficiariaAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'situacao_gravidez', 'data_nascimento', 'data_cadastro')
    search_fields = ('nome_completo', 'telefone', 'endereco')
    list_filter = ('data_cadastro',)
    fieldsets = (
        (None, {
            'fields': ('nome_completo', 'data_nascimento', 'telefone', 'endereco')
        }),
        ('Informações Adicionais', {
            'fields': ('situacao_gravidez', 'historico_medico', 'necessidades')
        }),
        ('Conta de Usuário (Opcional)', {
            'fields': ('user',),
            'classes': ('collapse',)
        }),
    )

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cargo', 'data_cadastro')
    search_fields = ('nome_completo', 'cargo')
    list_filter = ('cargo', 'data_cadastro')
    fieldsets = (
        (None, {
            'fields': ('user', 'nome_completo', 'cargo', 'telefone')
        }),
        ('Áreas de Atuação', {
            'fields': ('areas_interesse',)
        }),
    )

@admin.register(BalancoFinanceiro)
class BalancoFinanceiroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao')
    search_fields = ('titulo', 'descricao')
    readonly_fields = ('data_publicacao',)

@admin.register(PoliticaTransparencia)
class PoliticaTransparenciaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao')
    search_fields = ('titulo', 'documento')
    readonly_fields = ('data_publicacao',)

# ... (Mantenha todos os registros de admin existentes aqui) ...

@admin.register(CasoDeAjuda)
class CasoDeAjudaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao')
    search_fields = ('titulo', 'descricao')
    list_filter = ('data_criacao',)
    readonly_fields = ('data_criacao',)

@admin.register(Acao)
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
    )
    readonly_fields = ('data_publicacao',)

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'data_recebimento')
    search_fields = ('nome', 'email', 'observacoes')
    list_filter = ('data_recebimento',)
    readonly_fields = ('data_recebimento',)

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'order')
    list_filter = ('category',)
    list_editable = ('order',)

@admin.register(Depoimento)
class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'texto')
    list_filter = ('ativo',)
    list_editable = ('ativo',)

@admin.register(StaticImage)
class StaticImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
