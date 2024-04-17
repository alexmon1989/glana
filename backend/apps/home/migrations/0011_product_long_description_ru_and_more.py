# Generated by Django 4.2.10 on 2024-03-29 12:33

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_producttype_title_ru_producttype_title_uk'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='long_description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Длинное описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='long_description_uk',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Длинное описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='short_description_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='short_description_uk',
            field=models.CharField(max_length=255, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_uk',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
    ]
