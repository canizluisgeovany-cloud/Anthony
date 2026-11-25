from django import forms
from .models import Alumno, Maestro, Personal, Aula, Curso, Inscripcion, Asistencia


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = "__all__"

        widgets = {
            "fecha_nacimiento": forms.DateInput(
                attrs={"type": "date"}
            ),
            "direccion": forms.Textarea(
                attrs={"rows": 3}
            ),
        }


class MaestroForm(forms.ModelForm):
    class Meta:
        model = Maestro
        fields = "__all__"


class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = "__all__"


class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = "__all__"


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"


class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = "__all__"


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = "__all__"