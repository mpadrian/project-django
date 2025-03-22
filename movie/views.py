from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import movie

# Create your views here.

class MovieListView(ListView):
    model = Movie
    template_name = 'Movies/movie_list.html'

def lista_peliculas(request):
    peliculas = Movie.objects.all()
    return render(request, 'Movies/movie_list.html', {'peliculas': peliculas})

def detalle_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Movie, id=pelicula_id)
    return render(request, 'Movies/movie_detail.html', {'pelicula': pelicula})