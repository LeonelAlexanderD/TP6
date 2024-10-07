from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    cantidad_horas = models.PositiveSmallIntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    edad = models.PositiveSmallIntegerField()
    nota_curso = models.DecimalField(max_digits=4, decimal_places=2) 
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE) 
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}, Curso: {self.curso.nombre}, Nota: {self.nota_curso}"
    
