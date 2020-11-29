from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=150)
    premiere = models.IntegerField(default=2000)
    image = models.URLField(help_text="De imdb mismo")
    summary = models.TextField(help_text="Descripción corta")

    class Meta:
        ordering = ['title']
