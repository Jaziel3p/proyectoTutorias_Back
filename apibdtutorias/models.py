from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    rfc = models.CharField(max_length=13)
    periodo = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)


# Tablas para el formato de pdf del REPORTE SEMESTRAL DEL TUTOR

class TutorRep(models.Model):
    Nombre = models.CharField(max_length=70)
    fecha = models.CharField(max_length=50)
    ProgramaEducativo = models.CharField(max_length=45)
    Grupo = models.CharField(max_length=45)
    Hora = models.CharField(max_length=45)


class Almuno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    no_de_control = models.IntegerField(max_length=8, unique=True, null=True)
    nip = models.CharField(max_length=4, null=True)
    TotorF = models.ForeignKey(Tutor, on_delete=models.CASCADE, default=1)
    # # Devolcemos el no_de_control del alumno
    # def __str__(self):
    #     return self.no_de_control


class HorasAlumno(models.Model):
    Matricula = models.IntegerField()
    TutoríaGrupal = models.CharField(max_length=45)
    TutoríaIndividua = models.CharField(max_length=45)
    EstudiantesCanalizadosEnElSemestre = models.CharField(max_length=45)
    TotalHorasAcumuladas = models.CharField(max_length=45)
    ÁreaCanalizada = models.CharField(max_length=45)
    AlumnoF = models.ForeignKey(Almuno, on_delete=models.CASCADE)