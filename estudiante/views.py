from django.shortcuts import get_object_or_404, render

from estudiante.models import Estudiante, Curso
# Create your views here.

def index(request):
    return render(request, 'estudiante/index.html')


def alta_estudiante(request):
    return render(request, 'estudiante/alta_estudiante.html')


def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'estudiante/lista_cursos.html', {'cursos': cursos})

def listar_estudiantes(request):    
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiante/lista_estudiantes.html', {'estudiantes': estudiantes})

def estudiante_mayores(request, edad):
    estudiantes = Estudiante.objects.filter(edad__gt=edad)
    return render(request, 'estudiante/mayores.html', {'estudiantes': estudiantes})

def mostrar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    estudiantes = Estudiante.objects.filter(curso = curso)
    return render(request, 'estudiante/curso.html', {'curso': curso, 'estudiantes': estudiantes})