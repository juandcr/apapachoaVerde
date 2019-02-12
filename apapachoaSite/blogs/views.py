from django.shortcuts import render,get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Post,Category
# Create your views here.

class PostListView(ListView):
    model= Post
    paginate_by= 5


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, "blogs/category.html", {'category':category})


