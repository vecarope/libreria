from django.shortcuts import render
from django.db.models import Q
from .models import Libro, Autor, Editorial


# vista home
def home(request):
    queryset = request.GET.get('buscar')
    titulo = request.GET.get('titulo')
    autor = request.GET.get('autor')
    editorial = request.GET.get('editorial')
    libros = Libro.objects.select_related('autor', 'editorial').all()
    autores = Autor.objects.values_list('nombre', flat=True).distinct()
    editoriales = Editorial.objects.values_list('nombre', flat=True).distinct()

    if queryset:
        if ' ' in queryset:
            # filtro de busqueda compuesta
            palabras = queryset.lower().split()
            for palabra in palabras:
                libros = libros.filter(
                    Q(titulo__icontains=palabra)
                ).distinct()
        else:
            # filtro con una sola palabra
            queryset = queryset.lower()
            libros = libros.filter(
                Q(titulo__contains=queryset)
            ).distinct()


    else:
    # filtro individual por titulo, autor y editorial
        if titulo:
          libros = libros.filter(titulo__icontains=titulo)
        if autor:
          libros = libros.filter(autor__nombre__icontains=autor)
        if editorial:
          libros = libros.filter(editorial__nombre__icontains=editorial)

    return render(request, 'app/home.html', {'libros': libros,'autores': autores, 'editoriales':editoriales})
