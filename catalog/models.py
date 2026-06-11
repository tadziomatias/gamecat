from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=200, unique=True) # evita jogo duplicado
    platform = models.CharField(max_length=60) # ex.: "SNES"
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.platform})"

class GameHash(models.Model):
    game = models.ForeignKey(Game, related_name="hashes", on_delete=models.CASCADE)
    md5 = models.CharField(max_length=32, unique=True)
    region = models.CharField(max_length=40, blank=True)
    label = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.game.title} [{self.region or '?'}]"
    