from django.urls import path, include
from django.conf import settings
from .views import MovieListView
from movie import views
from django.conf.urls.static import static

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
    path('pelicula/<int:pelicula_id>/', views.detalle_pelicula, name='detalle_pelicula'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)