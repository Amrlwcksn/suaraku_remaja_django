from django.db import models

class Cerita(models.Model):
    nama = models.CharField(max_length=100)
    judul = models.CharField(max_length=200)
    isi_cerita = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul
