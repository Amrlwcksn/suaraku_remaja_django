from django.urls import path
from . import views

app_name = 'remaja_sehat'  # untuk namespace

urlpatterns = [
    path('', views.list_artikel, name='list_artikel'),
    path('<slug:slug>/', views.detail_artikel, name='detail_artikel'),
]
