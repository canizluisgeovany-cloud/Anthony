
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),

    # ALUMNOS
    path("alumnos/", views.alumno_lista, name="alumno_lista"),
    path("alumnos/crear/", views.alumno_crear, name="alumno_crear"),
    path("alumnos/editar/<int:pk>/", views.alumno_editar, name="alumno_editar"),
    path("alumnos/eliminar/<int:pk>/", views.alumno_eliminar, name="alumno_eliminar"),

    # MAESTROS
    path("maestros/", views.maestro_lista, name="maestro_lista"),
    path("maestros/crear/", views.maestro_crear, name="maestro_crear"),
    path("maestros/editar/<int:pk>/", views.maestro_editar, name="maestro_editar"),
    path("maestros/eliminar/<int:pk>/", views.maestro_eliminar, name="maestro_eliminar"),

    # PERSONAL
    path("personal/", views.personal_lista, name="personal_lista"),
    path("personal/crear/", views.personal_crear, name="personal_crear"),
    path("personal/editar/<int:pk>/", views.personal_editar, name="personal_editar"),
    path("personal/eliminar/<int:pk>/", views.personal_eliminar, name="personal_eliminar"),

    # AULAS
    path("aulas/", views.aula_lista, name="aula_lista"),
    path("aulas/crear/", views.aula_crear, name="aula_crear"),
    path("aulas/editar/<int:pk>/", views.aula_editar, name="aula_editar"),
    path("aulas/eliminar/<int:pk>/", views.aula_eliminar, name="aula_eliminar"),

    # CURSOS
    path("cursos/", views.curso_lista, name="curso_lista"),
    path("cursos/crear/", views.curso_crear, name="curso_crear"),
    path("cursos/editar/<int:pk>/", views.curso_editar, name="curso_editar"),
    path("cursos/eliminar/<int:pk>/", views.curso_eliminar, name="curso_eliminar"),

    # INSCRIPCIONES
    path("inscripciones/", views.inscripcion_lista, name="inscripcion_lista"),
    path("inscripciones/crear/", views.inscripcion_crear, name="inscripcion_crear"),
    path("inscripciones/editar/<int:pk>/", views.inscripcion_editar, name="inscripcion_editar"),
    path("inscripciones/eliminar/<int:pk>/", views.inscripcion_eliminar, name="inscripcion_eliminar"),

    # ASISTENCIA
    path("asistencia/", views.asistencia_lista, name="asistencia_lista"),
    path("asistencia/crear/", views.asistencia_crear, name="asistencia_crear"),
    path("asistencia/editar/<int:pk>/", views.asistencia_editar, name="asistencia_editar"),
    path("asistencia/eliminar/<int:pk>/", views.asistencia_eliminar, name="asistencia_eliminar"),
]
