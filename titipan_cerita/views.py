from django.shortcuts import render, get_object_or_404
from .models import Cerita

def list_cerita(request):
    cerita = Cerita.objects.all().order_by('-tanggal_dibuat')
    return render(request, 'titipan_cerita/list.html', {'cerita': cerita})

def detail_cerita(request, slug):
    cerita = get_object_or_404(Cerita, slug=slug)
    return render(request, 'titipan_cerita/detail.html', {'cerita': cerita})
