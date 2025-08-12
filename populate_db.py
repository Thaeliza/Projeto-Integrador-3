import os
import django
from django.core.files.base import ContentFile
import random

# Configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projetosarah.settings')
django.setup()

# Importa os modelos
from main.models import CasoDeAjuda, Acao, Depoimento, CarouselImage

def create_dummy_image(name, size=(800, 600)):
    """Cria um arquivo de imagem fictício em memória."""
    try:
        from PIL import Image, ImageDraw, ImageFont
        
        # Gera uma imagem em memória
        img = Image.new('RGB', size, 'gray')
        d = ImageDraw.Draw(img)
        
        try:
            # Tenta usar a fonte padrão do sistema
            font = ImageFont.truetype("arial.ttf", 30)
        except IOError:
            # Fallback para a fonte padrão do PIL se a fonte não for encontrada
            font = ImageFont.load_default()
        
        d.text((10, 10), name, fill='white', font=font)
        
        f = ContentFile(b'')
        img.save(f, 'JPEG')
        f.seek(0)
        return f
    except ImportError:
        # Retorna um arquivo vazio se o PIL não estiver instalado
        print("Atenção: A biblioteca Pillow (PIL) não está instalada. As imagens não serão geradas.")
        print("Para gerar imagens fictícias, instale com: pip install Pillow")
        return ContentFile(b'')


def populate():
    """
    Função principal para popular o banco de dados com dados de exemplo.
    """
    print("Iniciando o povoamento do banco de dados...")

    # --- Deleta os dados existentes para evitar duplicatas ---
    print("Limpando dados antigos...")
    CasoDeAjuda.objects.all().delete()
    Acao.objects.all().delete()
    Depoimento.objects.all().delete()
    CarouselImage.objects.all().delete()
    print("Dados antigos removidos.")
    
    # --- Cria dados de exemplo ---

    # Casos de Ajuda
    casos = [
        {'titulo': 'Maria, 16 anos - Ajuda com Enxoval', 'descricao': 'Maria precisa de ajuda com itens básicos para o enxoval do seu bebê. Ela está no 7º mês de gestação.'},
        {'titulo': 'Julia, 17 anos - Suporte Psicológico', 'descricao': 'Julia e sua família precisam de apoio psicológico e orientação para lidar com a gravidez na adolescência.'},
        {'titulo': 'Camila, 18 anos - Educação e Capacitação', 'descricao': 'Camila busca cursos profissionalizantes para garantir um futuro melhor para ela e seu filho após o nascimento.'},
    ]
    for caso_data in casos:
        imagem_file = create_dummy_image(caso_data['titulo'], size=(1024, 768))
        caso = CasoDeAjuda.objects.create(
            titulo=caso_data['titulo'],
            descricao=caso_data['descricao']
        )
        caso.imagem.save(f"caso_{caso.id}.jpg", imagem_file)
    print(f"✅ {len(casos)} Casos de Ajuda criados.")

    # Ações
    acoes = [
        {'titulo': 'Mutirão de Arrecadação de Roupas', 'descricao_breve': 'Mutirão para arrecadar roupas e itens de higiene para as futuras mamães.','descricao_completa': 'Este evento anual mobiliza a comunidade para arrecadar doações essenciais. Sua participação é vital para o nosso sucesso e para o bem-estar das jovens mães. Junte-se a nós para fazer a diferença!'},
        {'titulo': 'Palestra sobre Cuidados Pré-Natais', 'descricao_breve': 'Nossas voluntárias organizaram uma palestra com uma médica para falar sobre a importância do pré-natal.','descricao_completa': 'A palestra foi um sucesso! Abordamos temas importantes como nutrição na gravidez, exercícios e a importância do acompanhamento médico regular para garantir uma gestação saudável.'},
        {'titulo': 'Jantar Beneficente Anual', 'descricao_breve': 'Um jantar especial para arrecadar fundos para o Projeto Sarah e seus programas.','descricao_completa': 'O jantar beneficente é nosso principal evento de arrecadação de fundos. Com a ajuda da comunidade e de parceiros, conseguimos financiar nossos projetos de educação e saúde por todo o ano.'},
    ]
    for acao_data in acoes:
        imagem_file = create_dummy_image(acao_data['titulo'], size=(800, 600))
        acao = Acao.objects.create(
            titulo=acao_data['titulo'],
            descricao_breve=acao_data['descricao_breve'],
            descricao_completa=acao_data['descricao_completa']
        )
        acao.imagem.save(f"acao_{acao.id}.jpg", imagem_file)
    print(f"✅ {len(acoes)} Ações criadas.")

    # Depoimentos
    depoimentos = [
        {'nome': 'Ana P., beneficiada', 'texto': 'O Projeto Sarah mudou minha vida e me deu esperança para seguir em frente com meu bebê.'},
        {'nome': 'Carlos S., voluntário', 'texto': 'Fazer parte dessa equipe é gratificante. O impacto do nosso trabalho é visível no dia a dia.'},
        {'nome': 'Mariana R., doadora', 'texto': 'Sempre quis ajudar e encontrei no Projeto Sarah a transparência e seriedade que buscava para minhas doações.'},
    ]
    for depoimento_data in depoimentos:
        Depoimento.objects.create(**depoimento_data)
    print(f"✅ {len(depoimentos)} Depoimentos criados.")

    # Imagens do Carrossel (Exemplo)
    carousel_images_data = [
        {'title': 'Nossa Missão em Ação', 'description': 'Transformando vidas através do apoio.', 'category': 'home1', 'order': 1},
        {'title': 'Seja um Voluntário', 'description': 'Junte-se a nós e faça a diferença!', 'category': 'home1', 'order': 2},
        {'title': 'Doações que Salvam Vidas', 'description': 'Sua ajuda é a nossa força.', 'category': 'home2', 'order': 1},
    ]
    for image_data in carousel_images_data:
        imagem_file = create_dummy_image(image_data['title'], size=(1920, 600))
        image = CarouselImage.objects.create(
            title=image_data['title'],
            description=image_data['description'],
            category=image_data['category'],
            order=image_data['order']
        )
        image.image.save(f"carousel_{image.id}.jpg", imagem_file)
    print(f"✅ {len(carousel_images_data)} Imagens de carrossel criadas.")

    print("\n✅ Povoamento concluído com sucesso!")

if __name__ == '__main__':
    populate()
