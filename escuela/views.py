
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .models import Alumno, Maestro, Personal, Aula, Curso, Inscripcion, Asistencia
from .forms import (
    AlumnoForm, MaestroForm, PersonalForm, AulaForm,
    CursoForm, InscripcionForm, AsistenciaForm
)


@login_required
def dashboard(request):
    return render(request, "escuela/dashboard.html")


# CRUD DE ALUMNOS

@login_required
def alumno_lista(request):
    busqueda = request.GET.get("buscar", "")
    alumnos = Alumno.objects.all().order_by("nombres")

    if busqueda:
        alumnos = alumnos.filter(
            Q(nombres__icontains=busqueda) |
            Q(apellidos__icontains=busqueda) |
            Q(codigo__icontains=busqueda)
        )

    paginator = Paginator(alumnos, 10)
    alumnos = paginator.get_page(request.GET.get("page"))

    return render(request, "escuela/alumnos/lista.html", {
        "alumnos": alumnos, "buscar": busqueda
    })


@login_required
def alumno_crear(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("alumno_lista")
    else:
        form = AlumnoForm()

    return render(request, "escuela/alumnos/formulario.html", {
        "form": form, "titulo": "Registrar alumno"
    })


@login_required
def alumno_editar(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == "POST":
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect("alumno_lista")
    else:
        form = AlumnoForm(instance=alumno)

    return render(request, "escuela/alumnos/formulario.html", {
        "form": form, "titulo": "Editar alumno"
    })


@login_required
def alumno_eliminar(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == "POST":
        alumno.delete()
        return redirect("alumno_lista")

    return render(request, "escuela/alumnos/eliminar.html", {
        "alumno": alumno
    })


# CRUD DE MAESTROS

@login_required
def maestro_lista(request):
    busqueda = request.GET.get("buscar", "")
    maestros = Maestro.objects.all().order_by("nombres")

    if busqueda:
        maestros = maestros.filter(
            Q(nombres__icontains=busqueda) |
            Q(apellidos__icontains=busqueda) |
            Q(codigo__icontains=busqueda)
        )

    paginator = Paginator(maestros, 10)
    maestros = paginator.get_page(request.GET.get("page"))

    return render(request, "escuela/maestros/lista.html", {
        "maestros": maestros, "buscar": busqueda
    })


@login_required
def maestro_crear(request):
    if request.method == "POST":
        form = MaestroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("maestro_lista")
    else:
        form = MaestroForm()

    return render(request, "escuela/maestros/formulario.html", {
        "form": form, "titulo": "Registrar maestro"
    })


@login_required
def maestro_editar(request, pk):
    maestro = get_object_or_404(Maestro, pk=pk)
    if request.method == "POST":
        form = MaestroForm(request.POST, instance=maestro)
        if form.is_valid():
            form.save()
            return redirect("maestro_lista")
    else:
        form = MaestroForm(instance=maestro)

    return render(request, "escuela/maestros/formulario.html", {
        "form": form, "titulo": "Editar maestro"
    })


@login_required
def maestro_eliminar(request, pk):
    maestro = get_object_or_404(Maestro, pk=pk)
    if request.method == "POST":
        maestro.delete()
        return redirect("maestro_lista")

    return render(request, "escuela/maestros/eliminar.html", {
        "maestro": maestro
    })


# CRUD DE PERSONAL

@login_required
def personal_lista(request):
    busqueda = request.GET.get("buscar", "")
    personal = Personal.objects.all().order_by("nombres")

    if busqueda:
        personal = personal.filter(
            Q(nombres__icontains=busqueda) |
            Q(apellidos__icontains=busqueda) |
            Q(codigo__icontains=busqueda) |
            Q(cargo__icontains=busqueda)
        )

    paginator = Paginator(personal, 10)
    personal = paginator.get_page(request.GET.get("page"))

    return render(request, "escuela/personal/lista.html", {
        "personal": personal, "buscar": busqueda
    })


@login_required
def personal_crear(request):
    if request.method == "POST":
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("personal_lista")
    else:
        form = PersonalForm()

    return render(request, "escuela/personal/formulario.html", {
        "form": form, "titulo": "Registrar personal"
    })


@login_required
def personal_editar(request, pk):
    persona = get_object_or_404(Personal, pk=pk)
    if request.method == "POST":
        form = PersonalForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect("personal_lista")
    else:
        form = PersonalForm(instance=persona)

    return render(request, "escuela/personal/formulario.html", {
        "form": form, "titulo": "Editar personal"
    })


@login_required
def personal_eliminar(request, pk):
    persona = get_object_or_404(Personal, pk=pk)
    if request.method == "POST":
        persona.delete()
        return redirect("personal_lista")

    return render(request, "escuela/personal/eliminar.html", {
        "persona": persona
    })


# CRUD DE AULAS

@login_required
def aula_lista(request):
    busqueda = request.GET.get("buscar", "")
    aulas = Aula.objects.all().order_by("nombre")

    if busqueda:
        aulas = aulas.filter(
            Q(nombre__icontains=busqueda) |
            Q(ubicacion__icontains=busqueda)
        )

    paginator = Paginator(aulas, 10)
    aulas = paginator.get_page(request.GET.get("page"))

    return render(request, "escuela/aulas/lista.html", {
        "aulas": aulas, "buscar": busqueda
    })


@login_required
def aula_crear(request):
    if request.method == "POST":
        form = AulaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("aula_lista")
    else:
        form = AulaForm()

    return render(request, "escuela/aulas/formulario.html", {
        "form": form, "titulo": "Registrar aula"
    })


@login_required
def aula_editar(request, pk):
    aula = get_object_or_404(Aula, pk=pk)
    if request.method == "POST":
        form = AulaForm(request.POST, instance=aula)
        if form.is_valid():
            form.save()
            return redirect("aula_lista")
    else:
        form = AulaForm(instance=aula)

    return render(request, "escuela/aulas/formulario.html", {
        "form": form, "titulo": "Editar aula"
    })


@login_required
def aula_eliminar(request, pk):
    aula = get_object_or_404(Aula, pk=pk)
    if request.method == "POST":
        aula.delete()
        return redirect("aula_lista")

    return render(request, "escuela/aulas/eliminar.html", {
        "aula": aula
    })


# CRUD DE CURSOS

@login_required
def curso_lista(request):
    busqueda = request.GET.get("buscar", "")
    cursos = Curso.objects.all().order_by("nombre")

    if busqueda:
        cursos = cursos.filter(
            Q(nombre__icontains=busqueda) |
            Q(codigo__icontains=busqueda)
        )

    paginator = Paginator(cursos, 10)
    cursos = paginator.get_page(request.GET.get("page"))

    return render(request, "escuela/cursos/lista.html", {
        "cursos": cursos, "buscar": busqueda
    })


@login_required
def curso_crear(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("curso_lista")
    else:
        form = CursoForm()

    return render(request, "escuela/cursos/formulario.html", {
        "form": form, "titulo": "Registrar curso"
    })


@login_required
def curso_editar(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect("curso_lista")
    else:
        form = CursoForm(instance=curso)

    return render(request, "escuela/cursos/formulario.html", {
        "form": form, "titulo": "Editar curso"
    })


@login_required
def curso_eliminar(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == "POST":
        curso.delete()
        return redirect("curso_lista")

    return render(request, "escuela/cursos/eliminar.html", {
        "curso": curso
    })


# CRUD DE INSCRIPCIONES

@login_required
def inscripcion_lista(request):
    busqueda = request.GET.get("buscar", "")
    inscripciones = Inscripcion.objects.all().order_by("-fecha_inscripcion")

    if busqueda:
        inscripciones = inscripciones.filter(
            Q(alumno__nombres__icontains=busqueda) |
            Q(alumno__apellidos__icontains=busqueda) |
            Q(curso__nombre__icontains=busqueda)
        )

    paginator = Paginator(inscripciones, 10)
    inscripciones = paginator.get_page(request.GET.get("page"))

    return render(request, "escuela/inscripciones/lista.html", {
        "inscripciones": inscripciones, "buscar": busqueda
    })


@login_required
def inscripcion_crear(request):
    if request.method == "POST":
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inscripcion_lista")
    else:
        form = InscripcionForm()

    return render(request, "escuela/inscripciones/formulario.html", {
        "form": form, "titulo": "Registrar inscripción"
    })


@login_required
def inscripcion_editar(request, pk):
    inscripcion = get_object_or_404(Inscripcion, pk=pk)
    if request.method == "POST":
        form = InscripcionForm(request.POST, instance=inscripcion)
        if form.is_valid():
            form.save()
            return redirect("inscripcion_lista")
    else:
        form = InscripcionForm(instance=inscripcion)

    return render(request, "escuela/inscripciones/formulario.html", {
        "form": form, "titulo": "Editar inscripción"
    })


@login_required
def inscripcion_eliminar(request, pk):
    inscripcion = get_object_or_404(Inscripcion, pk=pk)
    if request.method == "POST":
        inscripcion.delete()
        return redirect("inscripcion_lista")

    return render(request, "escuela/inscripciones/eliminar.html", {
        "inscripcion": inscripcion
    })


# CRUD DE ASISTENCIA

@login_required
def asistencia_lista(request):
    busqueda = request.GET.get("buscar", "")
    asistencias = Asistencia.objects.all().order_by("-fecha")

    if busqueda:
        asistencias = asistencias.filter(
            Q(alumno__nombres__icontains=busqueda) |
            Q(alumno__apellidos__icontains=busqueda) |
            Q(curso__nombre__icontains=busqueda)
        )

    paginator = Paginator(asistencias, 10)
    asistencias = paginator.get_page(request.GET.get("page"))

    return render(request, "escuela/asistencia/lista.html", {
        "asistencias": asistencias,
        "buscar": busqueda
    })


@login_required
def asistencia_crear(request):
    if request.method == "POST":
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("asistencia_lista")
    else:
        form = AsistenciaForm()

    return render(request, "escuela/asistencia/formulario.html", {
        "form": form,
        "titulo": "Registrar asistencia"
    })


@login_required
def asistencia_editar(request, pk):
    asistencia = get_object_or_404(Asistencia, pk=pk)

    if request.method == "POST":
        form = AsistenciaForm(request.POST, instance=asistencia)
        if form.is_valid():
            form.save()
            return redirect("asistencia_lista")
    else:
        form = AsistenciaForm(instance=asistencia)

    return render(request, "escuela/asistencia/formulario.html", {
        "form": form,
        "titulo": "Editar asistencia"
    })


@login_required
def asistencia_eliminar(request, pk):
    asistencia = get_object_or_404(Asistencia, pk=pk)

    if request.method == "POST":
        asistencia.delete()
        return redirect("asistencia_lista")

    return render(request, "escuela/asistencia/eliminar.html", {
        "asistencia": asistencia
    })
