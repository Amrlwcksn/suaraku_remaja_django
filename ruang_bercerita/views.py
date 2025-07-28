from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CeritaForm

def kirim_cerita(request):
    if request.method == "POST":
        form = CeritaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cerita kamu berhasil dikirim! 🎉")
            return redirect('ruang_bercerita:kirim')
    else:
        form = CeritaForm()
    return render(request, 'ruang_bercerita/kirim_cerita.html', {'form': form})
