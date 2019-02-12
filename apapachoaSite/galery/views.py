from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Photo

# Create your views here.
class PhotoGaleryListView(ListView):
    model= Photo    
