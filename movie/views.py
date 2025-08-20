from django.shortcuts import render,redirect
from django.contrib.auth import  login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import Movie
# Create your views here.
def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('movie_list')
        else:
            form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})