from django.urls import path
from .views import PostListView
from . import views

blogs_patterns=[
    path('',PostListView.as_view(), name="posts"),
    path('category/<int:category_id>/',views.category, name="category"), 
]