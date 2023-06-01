from django.urls import path
from . import views

urlpatterns = [
    path('pesquisa', views.pesquisa, name='pesquisa')
]