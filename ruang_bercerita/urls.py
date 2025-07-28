from django.urls import path
from . import views

app_name = 'ruang_bercerita'

urlpatterns = [
    path('', views.kirim_cerita, name='kirim'),
]
