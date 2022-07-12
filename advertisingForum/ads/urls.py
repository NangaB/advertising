from django.urls import path
from . import views

urlpatterns = [
    path('ads/', views.home),
]