from .models import Film, FavoriteFilm
from rest_framework import serializers


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class FavoriteFilmSerializer(serializers.ModelSerializer):
    film = FilmSerializer()

    class Meta:
        model = FavoriteFilm
        fields = ['film']
