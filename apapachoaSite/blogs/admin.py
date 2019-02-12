from django.contrib import admin

from .models import Post,Category

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title',  'published')
    ordering = ('published',)
    search_fields = ('title','content')
    date_hierarchy = 'published'
    
     # Inyectamos nuestro fichero css
    class Media:
        css = {
            'all': ('blogs/css/custom_ckeditor.css',)
        }
        
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name',)


admin.site.register(Post, PostAdmin)   
admin.site.register(Category, CategoryAdmin)   
    


