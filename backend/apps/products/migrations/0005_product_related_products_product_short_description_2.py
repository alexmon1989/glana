# Generated by Django 4.2.10 on 2024-10-03 19:52

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_meta_description_product_meta_description_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='related_products',
            field=models.ManyToManyField(to='products.product', verbose_name='Связанные продукты'),
        ),
        migrations.AddField(
            model_name='product',
            name='short_description_2',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Краткое описание (страница товара)'),
        ),
    ]