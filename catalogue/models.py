from django.db import models

class Product(models.Model):
    """ ORM модель товаров"""
    title = models.TextField('Название продукта', max_length=1000,
                            help_text='Напишите что нибудь...', unique=True)
    description = models.TextField('Текст продукта', max_length=20000,
                            help_text='Напишите что нибудь...', default='Some desc')
    image = models.ImageField('Картинка',
                              upload_to='catalogue/images/',
                              blank=True,
                              null=True)
    category = models.ForeignKey('Category', blank=True, null=True,
                              on_delete=models.SET_NULL,
                              related_name='posts',
                              verbose_name='Категория',
                              help_text='Категория')
    price = models.TextField('Цена',blank=True, null= True)

    class Meta:
        """ Metaclass Products """
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title

class Category(models.Model):
    """ ORM модель категории"""
    category_title = models.TextField('Название категории', max_length=500,
                            help_text='Напишите что нибудь...')
    image = models.ImageField('Картинка',
                              upload_to='catalogue/category_images/',
                              blank=True,
                              null=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE,
                             related_name='products', null=True, blank=True)
    slug = models.SlugField('URL адрес', default='slug',
                            unique=True)

    class Meta:
        """ Metaclass Category """
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.category_title
