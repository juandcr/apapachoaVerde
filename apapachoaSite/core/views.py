from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Home 


class HomePageView(TemplateView):
    template_name= "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home'] = Home.objects.get(title='home')
        return context
    
class ContactPageView(TemplateView):
    template_name= "core/contact.html"
    

class AboutView(TemplateView):
    template_name='core/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = Home.objects.get(title='acerca')
        return context