from django.db import models


class Alumno(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dpi = models.CharField(max_length=20, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    correo = models.EmailField(blank=True)
    direccion = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombres} {self.apellidos}"


class Maestro(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    correo = models.EmailField(blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Personal(models.Model):
    class Cargo(models.TextChoices):
        GUARDIA = "GUARDIA", "Guardia"
        SECRETARIA = "SECRETARIA", "Secretaría"
        LICENCIADO = "LICENCIADO", "Licenciado"
        DIRECTOR = "DIRECTOR", "Director"
        OTRO = "OTRO", "Otro"

    codigo = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cargo = models.CharField(max_length=20, choices=Cargo.choices)
    telefono = models.CharField(max_length=20, blank=True)
    correo = models.EmailField(blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.get_cargo_display()}"


class Aula(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    ubicacion = models.CharField(max_length=150, blank=True)
    capacidad = models.PositiveIntegerField(default=30)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    duracion_horas = models.PositiveIntegerField(default=0)
    maestro = models.ForeignKey(
        Maestro,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="cursos"
    )
    aula = models.ForeignKey(
        Aula,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="cursos"
    )
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Inscripcion(models.Model):
    class Estado(models.TextChoices):
        ACTIVA = "ACTIVA", "Activa"
        FINALIZADA = "FINALIZADA", "Finalizada"
        RETIRADA = "RETIRADA", "Retirada"

    alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE,
        related_name="inscripciones"
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name="inscripciones"
    )
    fecha_inscripcion = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=15,
        choices=Estado.choices,
        default=Estado.ACTIVA
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["alumno", "curso"],
                name="inscripcion_unica_por_alumno_y_curso"
            )
        ]

    def __str__(self):
        return f"{self.alumno} - {self.curso}"


class Asistencia(models.Model):
    class Estado(models.TextChoices):
        PRESENTE = "PRESENTE", "Presente"
        AUSENTE = "AUSENTE", "Ausente"
        TARDE = "TARDE", "Llegó tarde"
        JUSTIFICADA = "JUSTIFICADA", "Ausencia justificada"

    alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE,
        related_name="asistencias"
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name="asistencias"
    )
    fecha = models.DateField()
    estado = models.CharField(
        max_length=15,
        choices=Estado.choices,
        default=Estado.PRESENTE
    )
    observaciones = models.TextField(blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["alumno", "curso", "fecha"],
                name="asistencia_unica_por_alumno_curso_fecha"
            )
        ]
        ordering = ["-fecha"]

    def __str__(self):
        return f"{self.alumno} - {self.fecha} - {self.get_estado_display()}"