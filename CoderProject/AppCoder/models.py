from django.db import models

# Create your models here.

class Curso(models.Model):
    name = models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiante(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

class Profesor(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    profession = models.CharField(max_length=40)

class Entregable(models.Model):
    name = models.CharField(max_length=40)
    submission_date = models.DateField()
    submitted = models.BooleanField()
