from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

class ArtikelRemajaSehat(models.Model):
    judul = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    konten = RichTextUploadingField()
    tanggal = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.judul)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.judul
