from typing import Any
from django.db import models

class Genero(models.Model):
    genero = models.CharField(max_length=255)
    def __str__(self):
        return self.genero
    
    
class Filmes(models.Model):
    titulo = models.CharField(max_length=255)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    ano = models.CharField(max_length=255)
    idioma = models.CharField(max_length=255)
    classif = models.CharField(max_length=255)
    