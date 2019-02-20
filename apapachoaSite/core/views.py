from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Home, Image


class HomePageView(TemplateView):
    template_name= "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        """
        context['home'] = Home.objects.get(title='home')
        context['bienvenido'] = Home.objects.get(title='bienvenido')
        context['titulo'] = Home.objects.get(title='titulo')
        context['imagen'] = Image.objects.get(title='imagen')
        """
        context['home'] = "home"
        context['bienvenido'] = "bienvenido"
        context['titulo'] = "titulo"
        context['imagen'] = "imagen"
        return context
    
class ContactPageView(TemplateView):
    template_name= "core/contact.html"
    

class AboutView(TemplateView):
    template_name='core/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['about'] = Home.objects.get(title='acerca')
        context['about'] = "acerca"
        return context