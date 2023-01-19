from django.urls import path

from estudiantes.views import (
    listar_estudiantes, listar_profesores, listar_cursos,
    crear_curso, buscar_cursos, crear_alumno, crear_profesor, buscar_profesores
)


urlpatterns = [
    path('alumnos/', listar_estudiantes, name="listar_alumnos"),
    path('profesores/', listar_profesores, name="listar_profesores"),
    path('cursos/', listar_cursos, name="listar_cursos"),
    path('crear-curso/', crear_curso, name="crear_curso"),
    path('buscar-cursos/', buscar_cursos, name="buscar_cursos"),
    path('crear-alumno/', crear_alumno, name="crear_alumno"), 
    path('crear-profesor/', crear_profesor, name="crear_profesor"),
    path('buscar-profesor/', buscar_profesores, name="buscar_profesor")
]
