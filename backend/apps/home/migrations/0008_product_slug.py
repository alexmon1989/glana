# Generated by Django 2.0.5 on 2018-06-22 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_product_long_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(null=True, verbose_name='Slug'),
        ),
    ]
