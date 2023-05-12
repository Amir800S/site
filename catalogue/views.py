from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView

from .models import Category, Product
from .utils import paginator

def index(request):
    """Главная страница."""
    category_list = Category.objects.all()
    page_obj = paginator(request, category_list)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'index.html', context)

def catalogue(request):
    """.Каталог."""
    category_list = Product.objects.all()
    page_obj = paginator(request, category_list)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'full_catalogue.html', context)

def catalogue_for_category(request, slug):
    """.Каталог для определенной категории."""
    category = get_object_or_404(Category, slug=slug)
    category_list = category.products.all()
    page_obj = paginator(request, category_list)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'catalogue.html', context)

def product_detail(request, product_id):
    """ Подробное чтение товара """
    get_product = get_object_or_404(Product, id=product_id)
    context = {
        'product': get_product,
    }
    return render(request, 'product_detail.html', context)

class Documents(TemplateView):
    """Шаблон раздела 'Документы'."""

    template_name = 'documents.html'
