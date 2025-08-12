from .models import CarouselImage
from .models import StaticImage

def carousel_base_context(request):
    images = CarouselImage.objects.filter(category='base')
    return {'carousel_base_images': images}



def static_images_context(request):
    """
    Injeta todas as imagens estáticas no contexto de todos os templates.
    """
    images_dict = {}
    for img in StaticImage.objects.all():
        images_dict[img.name] = img
    return {'static_images': images_dict}

