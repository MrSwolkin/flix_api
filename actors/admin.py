from django.contrib import admin
from .models import Actor


@admin.register(Actor)
class ActorsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "birthday", "nationality")
