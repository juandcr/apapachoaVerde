from django.db import models

# Create your models here.

class Photo(models.Model):
    title= models.CharField(max_length=200, verbose_name='Título')
    image=models.ImageField(verbose_name="Imagen", upload_to="galery", null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")    

    class Meta: 
        verbose_name="imágen"
        verbose_name_plural="imágenes"
        ordering=['-created']

    def __str__(self):
        return self.title