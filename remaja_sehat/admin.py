from django.contrib import admin
from .models import ArtikelRemajaSehat

@admin.register(ArtikelRemajaSehat)
class ArtikelRemajaSehatAdmin(admin.ModelAdmin):
    list_display = ('judul', 'tanggal', 'slug')
    prepopulated_fields = {'slug': ('judul',)}  # slug otomatis dari judul
    search_fields = ('judul', 'konten')  # bisa cari artikel dari judul/konten
    list_filter = ('tanggal',)  # filter berdasarkan tanggal

    class Media:
        css = {
            'all': ('https://cdn.jsdelivr.net/npm/ckeditor@4.20.0/skins/moono-lisa/editor.css',)
        }
