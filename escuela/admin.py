from django.contrib import admin
from .models import (
    Alumno,
    Maestro,
    Personal,
    Aula,
    Curso,
    Inscripcion,
    Asistencia,
)


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombres", "apellidos", "telefono", "activo")
    search_fields = ("codigo", "nombres", "apellidos", "dpi")
    list_filter = ("activo",)


@admin.register(Maestro)
class MaestroAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombres", "apellidos", "especialidad", "activo")
    search_fields = ("codigo", "nombres", "apellidos")
    list_filter = ("activo",)


@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombres", "apellidos", "cargo", "activo")
    search_fields = ("codigo", "nombres", "apellidos")
    list_filter = ("cargo", "activo")


@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "ubicacion", "capacidad")
    search_fields = ("nombre", "ubicacion")


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre", "maestro", "aula", "activo")
    search_fields = ("codigo", "nombre")
    list_filter = ("activo",)


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ("alumno", "curso", "fecha_inscripcion", "estado")
    search_fields = ("alumno__nombres", "alumno__apellidos", "curso__nombre")
    list_filter = ("estado", "fecha_inscripcion")


@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ("alumno", "curso", "fecha", "estado")
    search_fields = ("alumno__nombres", "alumno__apellidos", "curso__nombre")
    list_filter = ("estado", "fecha")