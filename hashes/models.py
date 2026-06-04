from django.db import models


class RomHash(models.Model):
    md5 = models.CharField(max_length=32, db_index=True)
    file_name = models.TextField()
    source = models.CharField(max_length=120, blank=True)
    imported_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['md5', 'file_name'],
                name='unique_md5_filename'
            )
        ]

    def __str__(self):
        return f"{self.md5[:8]}… {self.file_name[:40]}"
