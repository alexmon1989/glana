# Generated by Django 4.2.10 on 2024-05-10 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_product_long_description_ru_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductType',
        ),
    ]