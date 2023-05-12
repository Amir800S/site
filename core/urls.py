from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('about', views.AboutCompany.as_view(), name='about_company'),
    path('how_to_order', views.HowToOrder.as_view(), name='how_to_order'),
    path('contacts', views.Contacts.as_view(), name='contacts'),
]