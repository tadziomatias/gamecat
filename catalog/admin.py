from django.contrib import admin
from .models import Game, GameHash


class GameHashInline(admin.TabularInline):
    model = GameHash
    extra = 1

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "platform")
    search_fields = ("title", "hashes__md5")
    inlines = [GameHashInline]
