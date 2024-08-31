# Generated by Django 2.0.5 on 2018-05-10 13:16

import apps.home.models
from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype',
            name='slug',
            field=models.SlugField(default='', max_length=255, verbose_name='Slug (для url)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to=apps.products.utils.get_products_upload_to_folder, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='types',
            field=models.ManyToManyField(to='home.ProductType', verbose_name='Тип продукта'),
        ),
    ]
