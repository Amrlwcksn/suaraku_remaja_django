from django import forms
from .models import Cerita

class CeritaForm(forms.ModelForm):
    class Meta:
        model = Cerita
        fields = ['nama', 'judul', 'isi_cerita']
        widgets = {
            'nama': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Anonim jika tidak ingin diketahui'
            }),
            'judul': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Masukkan judul cerita'
            }),
            'isi_cerita': forms.Textarea(attrs={
                'class': 'w-full p-2 border rounded',
                'rows': 4,
                'placeholder': 'Tulis cerita Anda di sini...'
            }),
        }
