from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView

from .models import Category, Product
from .utils import paginator
from .forms import CallBackForm

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
    category_list = category.product.select_related('category').all()
    page_obj = paginator(request, category_list)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'catalogue.html', context)

def product_detail(request, product_id):
    """ Подробное чтение товара """
    get_product = get_object_or_404(Product, id=product_id)
    form = CallBackForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue:product_detail', id=product_id)
    context = {
        'product': get_product,
        'form': form
    }
    return render(request, 'product_detail.html', context)

def callback_send(request):
    form = CallBackForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'form_page.html', {'form': form})

class Documents(TemplateView):
    """Шаблон для раздела 'Документы'."""

    template_name = 'documents.html'
