from django.contrib import admin
from .models import Home

# Register your models here.
class HomeAdmin(admin.ModelAdmin):    
    list_display = ('title',  'text')           
    
     # Inyectamos nuestro fichero css
    class Media:
        css = {
            'all': ('blogs/css/custom_ckeditor.css',)
        }        



admin.site.register(Home, HomeAdmin) 

    
