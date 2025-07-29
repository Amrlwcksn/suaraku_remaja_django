from django.contrib import admin
from .models import Cerita

@admin.register(Cerita)
class CeritaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'judul','created_at')
    search_fields = ('nama', 'judul')
    list_filter = ('created_at',)
