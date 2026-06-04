from django.contrib import admin
from .models import RomHash

@admin.register(RomHash)
class RomHashAdmin(admin.ModelAdmin):
    list_display = ("md5", "file_name", "source", "imported_at")
    search_fields = ("md5", "file_name")
    list_filter = ("source",)