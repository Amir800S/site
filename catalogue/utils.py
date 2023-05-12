from django.conf import settings
from django.core.paginator import Paginator


def paginator(request, category_list):
    """ Paginator для приложения Catalogue"""
    paginator_get = Paginator(category_list, 15) # Количество товаров на странице
    page_number = request.GET.get('page')
    page_obj = paginator_get.get_page(page_number)

    return page_obj
