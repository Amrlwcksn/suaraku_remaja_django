from django.shortcuts import render, get_object_or_404
from .models import ArtikelRemajaSehat

def list_artikel(request):
    artikel = ArtikelRemajaSehat.objects.order_by('-tanggal')
    return render(request, 'remaja_sehat/list.html', {'artikel': artikel})

def detail_artikel(request, slug):
    artikel = get_object_or_404(ArtikelRemajaSehat, slug=slug)
    return render(request, 'remaja_sehat/detail.html', {'artikel': artikel})
