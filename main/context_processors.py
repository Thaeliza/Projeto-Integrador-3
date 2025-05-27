from .models import CarouselImage

def carousel_base_context(request):
    images = CarouselImage.objects.filter(category='base')
    return {'carousel_base_images': images}
