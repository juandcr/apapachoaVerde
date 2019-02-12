from django.urls import path
from .views import ProductListView,ProductDetailView

tienda_patterns=([
    path('',ProductListView.as_view(), name="store"),
    path('<int:pk>/<slug:slug>',ProductDetailView.as_view(), name="product"),
],"store")