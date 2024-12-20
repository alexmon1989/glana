# Generated by Django 4.2.10 on 2024-09-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_delete_product_delete_producttype'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactData',
        ),
        migrations.AlterField(
            model_name='pagedata',
            name='meta_description',
            field=models.TextField(blank=True, default=None, max_length=255, verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pagedata',
            name='meta_description_ru',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='pagedata',
            name='meta_description_uk',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='pagedata',
            name='meta_h1',
            field=models.CharField(blank=True, default=None, max_length=255, verbose_name='H1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pagedata',
            name='meta_h1_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='H1'),
        ),
        migrations.AlterField(
            model_name='pagedata',
            name='meta_h1_uk',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='H1'),
        ),
        migrations.AlterField(
            model_name='pagedata',
            name='meta_keywords',
            field=models.TextField(blank=True, default=None, max_length=255, verbose_name='Keywords'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pagedata',
            name='meta_keywords_ru',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Keywords'),
        ),
        migrations.AlterField(
            model_name='pagedata',
            name='meta_keywords_uk',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Keywords'),
        ),
        migrations.AlterField(
            model_name='pagedata',
            name='meta_title',
            field=models.CharField(blank=True, default=None, max_length=255, verbose_name='Title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pagedata',
            name='meta_title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='pagedata',
            name='meta_title_uk',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Title'),
        ),
    ]
