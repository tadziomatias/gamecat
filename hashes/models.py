from django.db import models


class RomHash(models.Model):
    md5 = models.CharField(max_length=32, db_index=True, unique=True)
    file_name = models.TextField()
    source = models.CharField(max_length=120, blank=True)
    imported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.md5[:8]}… {self.file_name[:40]}"
