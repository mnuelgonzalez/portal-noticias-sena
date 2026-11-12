from django.shortcuts import render
from .models import Noticia

def inicio(request):
    # Obtenemos todas las noticias ordenadas por fecha mas reciente primero
    noticias = Noticia.objects.all().order_by('-fecha')
    return render(request, 'app_noticia/inicio.html', {'noticias': noticias})

