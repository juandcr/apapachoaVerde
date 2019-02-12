from django.shortcuts import render
from .models import Product
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

class ProductListView(ListView):
    model = Product
    paginate_by= 10
    
class ProductDetailView(DetailView):
    model= Product