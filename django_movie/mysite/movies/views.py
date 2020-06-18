from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'movies/index.html',context)

def new(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:index')
    else :
        form = MovieForm()
    context = {
        'form' : form
    }
    return render(request, 'movies/form.html', context)

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie' : movie
    }
    return render(request, 'movies/detail.html', context)
    
def edit(request, movie_pk):
    movie = get_object_or_404(Movie, pk= movie_pk)
    movies = Movie.objects.get(pk=movie_pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movies)
        if form.is_valid():
            movies = form.save()
            return redirect('movies:detail',movie_pk )
    else :
        form = MovieForm(instance=movies)
    context = {
        'form' : form
    }
    return render(request, 'movies/form.html', context)

def delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movies = Movie.objects.get(pk=movie_pk).delete()
    return redirect('movies:index')
