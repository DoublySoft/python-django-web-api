from .models import Film
from .serializers import FilmSerializer
from rest_framework import viewsets


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
