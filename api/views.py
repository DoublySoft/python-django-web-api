from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Film, FavoriteFilm
from .serializers import FilmSerializer, FavoriteFilmSerializer
from rest_framework import viewsets, views, filters


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'premiere']
    ordering_fields = ['favorites']


class BookmarkFilmFavorite(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        film = get_object_or_404(Film, id=self.request.data.get('id', 0))
        favorite, created = FavoriteFilm.objects.get_or_create(film=film, user=request.user)

        # Por defecto suponemos que se crea bien
        content = {'id': film.id, 'favorite': True}

        # Si no se ha creado es que ya existe, entonces borramos el favorito
        if not created:
            favorite.delete()
            content['favorite'] = False

        return Response(content)


class FavoriteFilmList(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        favorite_films = FavoriteFilm.objects.filter(user=request.user)
        serializer = FavoriteFilmSerializer(favorite_films, many=True)

        return Response(serializer.data)
