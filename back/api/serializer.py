from rest_framework import serializers
from .models import Filmes, Genero


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['id', 'genero']

class FilmesSerializer(serializers.ModelSerializer):
    genero = GeneroSerializer()
    class Meta:
        model = Filmes
        fields = ['id', 'titulo', 'genero', 'ano', 'idioma', 'classif']
        
