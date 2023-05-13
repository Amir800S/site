from django.contrib import admin

from .models import Product, Category, CallBack

class ProductAdmin(admin.ModelAdmin):
    """Админ товаров."""
    list_display = (
        'title',
        'description',
        'image',
        'category',
        'document',
        'certificate',
        'price',
        'options',
        'characteristic',
    )
    list_editable = (
        'title','description','document',
        'certificate', 'image','category', 'price', 'options',
        'characteristic',
    )
    search_fields = ('title', 'price')
    list_display_links = None
    empty_value_display = '-пусто-'

class CategoryAdmin(admin.ModelAdmin):
    """ Админ категории."""
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

class CallBackAdmin(admin.ModelAdmin):
    """Админ заявок."""
    list_display = (
        'name',
        'phone_number',
        'message',
    )
    search_fields = ('name', 'phone_number', 'message',)
    list_display_links = None
    empty_value_display = '-пусто-'

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CallBack, CallBackAdmin)