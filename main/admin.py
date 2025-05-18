from django.contrib import admin
from .models import CasoDeAjuda,CarouselImage



class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)

admin.site.register(CarouselImage)
admin.site.register(CasoDeAjuda)