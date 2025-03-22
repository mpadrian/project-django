from django.contrib import admin
from .models import Movies

@admin.register(Movies)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'año_lanzamiento', 'genero', 'director', 'calificacion')
    list_filter = ('genero', 'año_lanzamiento')
    search_fields = ('titulo', 'director')