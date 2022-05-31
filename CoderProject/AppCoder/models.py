from django.db import models

# Create your models here.

class Curso(models.Model):
    name = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self) -> str:
        return self.name+' '+str(self.camada)

class Estudiante(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    def __str__(self) -> str:
        return self.name+' '+str(self.last_name)+' '+str(self.email)

class Profesor(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    profession = models.CharField(max_length=40)
    def __str__(self) -> str:
        return self.name+' '+str(self.last_name)+' '+str(self.email)+' '+str(self.profession)

class Entregable(models.Model):
    name = models.CharField(max_length=40)
    submission_date = models.DateField()
    submitted = models.BooleanField()
    def __str__(self) -> str:
        return self.name+' '+str(self.submission_date)+' '+str(self.submitted)
