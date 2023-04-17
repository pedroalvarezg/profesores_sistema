from django.db import models

class Materia(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=255)
    semestre = models.IntegerField()
    matricula = models.IntegerField()
    email = models.EmailField()
    grupo = models.CharField(max_length=255)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    temas_vistos = models.ManyToManyField('Tema', blank=True)

    def __str__(self):
        return self.nombre

class Tema(models.Model):
    nombre = models.CharField(max_length=255)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
