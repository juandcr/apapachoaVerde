from django.contrib import admin
from .models import Photo
# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title',)
    ordering = ('created',)
    search_fields = ('title',)      
    
    

admin.site.register(Photo, PhotoAdmin)
    


