from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from estudiantes.models import Estudiante, Profesor, Curso
from estudiantes.forms import CursoFormulario, AlumnoFormulario, ProfesorFormulario


def inicio(request):
    return render(
        request=request,
        template_name='estudiantes/inicio.html',
    )


def listar_estudiantes(request):
    ## Aqui iria la validacion del permiso lectura estudiantes
    contexto = {
        'estudiantes': Estudiante.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_estudiantes.html',
        context=contexto,
    )


def listar_profesores(request):
    contexto = {
        'profesores': Profesor.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_profesores.html',
        context=contexto,
    )


def listar_cursos(request):
    contexto = {
        'cursos': Curso.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_cursos.html',
        context=contexto,
    )



def crear_curso(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso = Curso(nombre=data['nombre'], comision=data['comision'])
            curso.save()
            url_exitosa = reverse('listar_cursos')
            return redirect(url_exitosa)
    else:  # GET
        formulario = CursoFormulario()
    return render(
        request=request,
        template_name='estudiantes/formulario_curso.html',
        context={'formulario': formulario},
    )

def crear_alumno(request):
    if request.method == "POST":
        formulario = AlumnoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            alumno = Estudiante(nombre=data['nombre'], apellido=data['apellido'],dni=data['dni'], email=data['email'])
            alumno.save()
            url_exitosa = reverse('listar_alumnos')
            return redirect(url_exitosa)
    else:  # GET
        formulario = AlumnoFormulario()
    return render(
        request=request,
        template_name='estudiantes/formulario_alumno.html',
        context={'formulario': formulario},
    )


def crear_profesor(request):
    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            profesor = Profesor(nombre=data['nombre'], apellido=data['apellido'],dni=data['dni'], profesion=data['profesion'])
            profesor.save()
            url_exitosa = reverse('listar_profesores')
            return redirect(url_exitosa)
    else:  # GET
        formulario = ProfesorFormulario()
    return render(
        request=request,
        template_name='estudiantes/formulario_profesor.html',
        context={'formulario': formulario},
    )



def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        cursos = Curso.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(comision__exact=data['busqueda'])
        )
        contexto = {
            'cursos': cursos
        }
        return render(
            request=request,
            template_name='estudiantes/lista_cursos.html',
            context=contexto,
        )


def buscar_profesores(request):
    if request.method == "POST":
        data = request.POST
        profesor = Profesor.objects.filter(
            Q(apellido__contains=data['busqueda']) | Q(profesion__contains=data['busqueda']))
        contexto = {
            'profesores': profesor
        }
        return render(
            request=request,
            template_name='estudiantes/lista_profesores.html',
            context=contexto,
        )
        
