from django.urls import path

from . import views

app_name = 'catalogue'

urlpatterns = [
    path('catalogue/', views.catalogue, name='full_catalogue'),
    path('catalogue/<slug:slug>/',
         views.catalogue_for_category, name='catalogue_for_category'),
    path('product_detail/<int:product_id>', views.product_detail, name='product_detail'),
    path('form/', views.callback_send, name='callback_send'), # Форма на странице товара
    path('documents/', views.Documents.as_view(), name='documents'),
    path('', views.index, name='index'),
]