from django.urls import path
from . import views

app_name = 'titipan_cerita'

urlpatterns = [
    path('', views.list_cerita, name='list_cerita'),
    path('<slug:slug>/', views.detail_cerita, name='detail_cerita'),
]
