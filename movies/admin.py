from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class AdminMovie(admin.ModelAdmin):
    list_display = ("id", "title", "genre", "release_date", "resume")
