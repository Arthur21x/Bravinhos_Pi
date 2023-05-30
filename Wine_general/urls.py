from django.urls import path
from . import views

urlpatterns = [
    path('Wine_general/<int:i>/', views.Wine_general, name='Wine Details')
]