from django.db import models

# Create your models here.

class Tutor(models.Model):
    rfc = models.CharField(max_length=13)
    periodo = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)