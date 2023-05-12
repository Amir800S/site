from django.contrib import admin

from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    """ Админ товаров """
    list_display = (
        'title',
        'description',
        'image',
        'category',
        'price',
    )
    list_editable = ('title','description', 'image','category', 'price')
    search_fields = ('title', 'price')
    list_display_links = None
    empty_value_display = '-пусто-'

class CategoryAdmin(admin.ModelAdmin):
    """ Админ категории """
    list_display = (
        'category_title',
        'image',
        'slug',
        'products',
    )
    list_editable = ('category_title', 'image', 'products', 'slug',)
    search_fields = ('category_title', 'products', 'slug',)
    list_display_links = None
    empty_value_display = '-пусто-'

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)