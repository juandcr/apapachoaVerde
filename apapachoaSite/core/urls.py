from django.urls import path
from .views import HomePageView,AboutView,ContactPageView

core_patterns=[
    path('',HomePageView.as_view(), name="home"),
    path('about/',AboutView.as_view(),name="about"), 
    path('contact/',ContactPageView.as_view(),name="contact")
]