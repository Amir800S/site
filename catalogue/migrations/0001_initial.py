# Generated by Django 4.2.1 on 2023-05-11 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(help_text='Напишите что нибудь...', max_length=5000, unique=True, verbose_name='Текст продукта')),
                ('image', models.ImageField(blank=True, null=True, upload_to='catalogue/images/', verbose_name='Картинка')),
                ('price', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.TextField(help_text='Напишите что нибудь...', max_length=500, verbose_name='Текст лота')),
                ('image', models.ImageField(blank=True, null=True, upload_to='catalogue/category_images/', verbose_name='Картинка')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='catalogue.product')),
            ],
        ),
    ]