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
                              related_name='product',
                              verbose_name='Категория',
                              help_text='Категория')
    document = models.FileField(upload_to='documents/', null=True,blank=True)
    certificate = models.FileField(upload_to='certificates/', null=True, blank=True)
    price = models.TextField('Цена',blank=True, null= True)
    characteristic = models.TextField('Характеристики', max_length=2500,
                            help_text='Напишите что нибудь...', null=True, blank=True)
    options = models.TextField('Параметры', max_length=2500,
                            help_text='Напишите что нибудь...', null=True, blank=True)

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
                             related_name='product', null=True, blank=True)
    slug = models.SlugField('URL адрес', default='slug',
                            unique=True)

    class Meta:
        """ Metaclass Category """
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.category_title

class CallBack(models.Model):
    """ ORM Callback модель """
    name = models.CharField('ФИО Клиента', max_length=70, blank=True, null=False,)
    phone_number = models.CharField('Номер клиента', max_length=70, null=False, blank=True,)
    message = models.TextField('Сообщение', max_length=500, null=False, blank=True,)

    class Meta:
        """ Metaclass CallBack """
        verbose_name_plural = 'Заявки на звонок'

    def __str__(self):
        return f'Клиент {self.name}, оставил сообщение {self.message}'