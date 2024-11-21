from django.db.models import Avg
from rest_framework import serializers
from .models import Movie
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer


class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"

    def validate_release_date(self, value):
        if value.year < 1800:
            raise serializers.ValidationError("A data de lançamento não pode ser anterior a 1990.")
        return value

    def validate_resume(self, value):
        if len(value) > 700:
            raise serializers.ValidationError("Resumo deve conter no máximo 200 caracteres.")
        return value


class MovieDetailSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    actors = ActorSerializer(many=True)
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "genre", "actors", "release_date", "rate", "resume"]

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg("stars"))["stars__avg"]
        if rate:
            return round(rate, 1)
        return rate


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movie_by_genre = serializers.ListField()
    total_review = serializers.IntegerField()
    avarage_stars = serializers.FloatField()