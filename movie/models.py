from django.db import models

# Modelo Movies
class Movies(models.Model):
    GENERO_CHOICES = [
        ('ACC', 'Acción'),
        ('COM', 'Comedia'),
        ('DRA', 'Drama'),
        ('TER', 'Terror'),
        ('SCI', 'Ciencia ficción'),
        ('ANI', 'Animación'),
        ('ROM', 'Romance'),
        ('DOC', 'Documental'),
    ]

    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción", blank=True, null=True)
    año_lanzamiento = models.PositiveIntegerField(verbose_name="Año de lanzamiento")
    genero = models.CharField(max_length=3, choices=GENERO_CHOICES, verbose_name="Género")
    duracion = models.PositiveIntegerField(verbose_name="Duración (minutos)", help_text="Duración en minutos")
    director = models.CharField(max_length=100, verbose_name="Director")
    calificacion = models.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        verbose_name="Calificación", 
        help_text="Calificación de 0.0 a 10.0"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    portada = models.ImageField(upload_to='portadas/', verbose_name="Portada", blank=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        ordering = ['-fecha_creacion']