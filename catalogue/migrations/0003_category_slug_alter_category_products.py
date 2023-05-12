# Generated by Django 4.2.1 on 2023-05-11 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='slug', unique=True, verbose_name='URL адрес'),
        ),
        migrations.AlterField(
            model_name='category',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='catalogue.product'),
        ),
    ]