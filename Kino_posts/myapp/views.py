from django.shortcuts import render, get_object_or_404
from .models import Artiles

# Create your views here.


def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/us.html")


def film_detail(request, film_id):
    film = get_object_or_404(Artiles, pk=film_id)
    return render(request, 'main/Film_info.html', {'el': film})  # Передаем объект фильма под именем 'el'
