from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display=('name','description','prize')
    ordering = ('created',)
    search_fields=('name',)

admin.site.register(Product,ProductAdmin)
