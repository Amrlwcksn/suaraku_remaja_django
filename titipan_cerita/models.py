from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField  # ✅ tambahkan ini!

class Cerita(models.Model):
    judul = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    konten = RichTextUploadingField()
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)
    tanggal_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.judul
