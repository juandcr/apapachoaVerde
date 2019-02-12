from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Product(models.Model):
    name= models.CharField(max_length=200, verbose_name='Producto')
    image=models.ImageField(verbose_name="Imagen", upload_to="galery", null=False, blank=False)
    productId= models.CharField(max_length=10, verbose_name='Clave de producto')
    description = RichTextField(verbose_name="Descripcion corta")
    largeDescription = RichTextField(verbose_name="Descripcion detallada")
    prize = models.FloatField(verbose_name="Precio")
    amount = models.IntegerField(verbose_name="Cantidad")
    paypalButton = models.TextField(verbose_name="Botón Paypal")
    available= models.BooleanField(verbose_name="Disponible")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")    
    
    class Meta: 
        verbose_name="Producto"
        verbose_name_plural="Productos"
        ordering=['-created']

    def __str__(self):
        return self.name