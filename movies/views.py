from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from .models import Movie
from reviews.models import Review
from .serializers import MovieModelSerializer, MovieStatsSerializer, MovieDetailSerializer


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission, )
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieDetailSerializer
        return MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission, )
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieDetailSerializer
        return MovieModelSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission, )
    queryset = Movie.objects.all()

    def get(self, request):
        # buscar os dados
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values(
            "genre__name").annotate(count=Count("id"))
        total_review = Review.objects.count()
        avarage_stars = Review.objects.aggregate(
            avg_stars=Avg("stars"))["avg_stars"]

        data = {
            "total_movies": total_movies,
            "movie_by_genre": movies_by_genre,
            "total_review": total_review,
            "avarage_stars": round(avarage_stars, 1) if avarage_stars else 0
        }
        serializer = MovieStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        return response.Response(serializer.validated_data, status=status.HTTP_200_OK)
