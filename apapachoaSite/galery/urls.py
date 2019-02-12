from django.urls import path
from .views import PhotoGaleryListView

galery_patterns=[
    path('',PhotoGaleryListView.as_view(), name="galery"),
 
]