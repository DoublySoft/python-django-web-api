from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, post_delete


class Film(models.Model):
    title = models.CharField(max_length=150)
    premiere = models.IntegerField(default=2000)
    image = models.URLField(help_text="De imdb mismo")
    summary = models.TextField(help_text="Descripción corta")
    favorites = models.IntegerField(default=0)

    class Meta:
        ordering = ['title']


class FavoriteFilm(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


def update_favorites(sender, instance, **kwargs):
    count = instance.pelicula.peliculafavorita_set.all().count()
    instance.pelicula.favorites = count
    instance.pelicula.save()


# en el post delete se pasa la copia de la instance que ya no existe
post_save.connect(update_favorites, sender=FavoriteFilm)
post_delete.connect(update_favorites, sender=FavoriteFilm)
