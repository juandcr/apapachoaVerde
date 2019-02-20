from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Home(models.Model):
    title= models.CharField(max_length=200, verbose_name='Título')    
    text = RichTextField(verbose_name="Contenido")

    class Meta: 
        verbose_name="Texto Inicio"
        verbose_name_plural="Textos inicio"        

    def __str__(self):
        return self.title

class Image(models.Model):
    title= models.CharField(max_length=200, verbose_name='Título')    
    image = models.ImageField(verbose_name="imágen inicio")

    class Meta: 
        verbose_name="imágen Inicio"
        verbose_name_plural="imagenes inicio"        

    def __str__(self):
        return self.title