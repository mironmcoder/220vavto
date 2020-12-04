# Generated by Django 3.0.2 on 2020-11-28 06:49

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название Фильтра')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('seo_meta_description', models.TextField(blank=True, default=None, null=True, verbose_name='SEO Meta описание к данному фильтру')),
                ('seo_key', models.TextField(blank=True, default=None, null=True, verbose_name='SEO ключи к данному Фильтру')),
                ('seo_title', models.TextField(blank=True, default=None, null=True, verbose_name='SEO тайтл страницы Фильтра')),
            ],
            options={
                'verbose_name': 'Фильтры',
                'verbose_name_plural': 'Фильтры',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название категории')),
                ('h1', models.CharField(default='title', max_length=100, verbose_name='h1 заголовок')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='h1')),
                ('seo_meta_description', models.TextField(blank=True, default=None, null=True, verbose_name='SEO Meta описание к данной категории')),
                ('seo_key', models.TextField(blank=True, default=None, null=True, verbose_name='SEO ключи к данному товару')),
                ('seo_title', models.TextField(blank=True, default=None, null=True, verbose_name='SEO тайтл страницы товара')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product.ProductCategory', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='ProductCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название товара')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('description', ckeditor.fields.RichTextField(blank=True, verbose_name='Подробное описание')),
                ('short_description', ckeditor.fields.RichTextField(blank=True, default=None, null=True, verbose_name='Краткое описание')),
                ('bottom_description', ckeditor.fields.RichTextField(blank=True, default=None, null=True, verbose_name='Дополнительное описание')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
                ('mod_date', models.DateField(auto_now=True, verbose_name='Обновление публикации')),
                ('price', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='Новая цена')),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='Старая цена')),
                ('image', models.ImageField(upload_to='products', verbose_name='Главное изображение карточки товара')),
                ('is_active', models.BooleanField(default=True, verbose_name='Публикация')),
                ('in_stock', models.BooleanField(default=True, verbose_name='Наличие товара')),
                ('seo_meta_description', models.TextField(blank=True, default=None, null=True, verbose_name='SEO Meta описание к данному товару')),
                ('seo_key', models.TextField(blank=True, default=None, null=True, verbose_name='SEO ключи к данному товару')),
                ('seo_title', models.TextField(blank=True, default=None, null=True, verbose_name='SEO тайтл страницы товара')),
                ('seo_alt_img', models.TextField(blank=True, default=None, null=True, verbose_name='SEO ALT Изображения товара')),
                ('category', mptt.fields.TreeManyToManyField(to='product.ProductCategory')),
                ('productfilter', models.ManyToManyField(to='product.ProductFilter', verbose_name='Фильтры')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='ImagesBottom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='products')),
                ('product', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.ProductCart', verbose_name='Изображения в нижней части карточки товара ')),
            ],
            options={
                'verbose_name': 'изображения',
                'verbose_name_plural': 'Изображения в нижней части карточки товара (Дополнительные)',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='products')),
                ('product', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.ProductCart', verbose_name='Дополнительные изображения')),
            ],
            options={
                'verbose_name': 'изображения',
                'verbose_name_plural': 'Дополнительные Изображения товара',
            },
        ),
    ]
