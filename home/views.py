from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriptionForm

def index(request):
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Terima kasih sudah subscribe!")
            return redirect("home:index")
    else:
        form = SubscriptionForm()

    return render(request, "home/index.html", {"form": form})
