from django.contrib import admin
from .models import Cerita

@admin.register(Cerita)
class CeritaAdmin(admin.ModelAdmin):
    list_display = ('judul', 'tanggal_dibuat', 'tanggal_update')
    prepopulated_fields = {'slug': ('judul',)}
