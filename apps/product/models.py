from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from unidecode import unidecode
from mptt.models import MPTTModel, TreeManyToManyField, TreeForeignKey
from ckeditor.fields import RichTextField

# Create your models here.

class ProductCategory(MPTTModel):
	title = models.CharField(max_length=100, verbose_name = "Название категории")
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name="Родитель")
	h1 = models.CharField(max_length=100, blank=True, null=True, verbose_name="h1 заголовок")
	slug = AutoSlugField(populate_from='h1')
	seo_meta_description = models.TextField(blank=True, null=True, default=None, verbose_name = "SEO Meta описание к данной категории")
	seo_key = models.TextField(blank=True, null=True, default=None, verbose_name = "SEO ключи к данному товару")
	seo_title = models.TextField(blank=True, null=True, default=None, verbose_name = "SEO тайтл страницы товара")

	def save(self, *args, **kwargs):
		if self.h1 is None:
			self.h1 = self.title
		super(ProductCategory, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

class ProductFilter(models.Model):
	title = models.CharField(max_length=100, verbose_name = "Название Фильтра")
	slug = AutoSlugField(populate_from='title')
	seo_meta_description = models.TextField(blank=True, null=True, default=None, verbose_name = "SEO Meta описание к данному фильтру")
	seo_key = models.TextField(blank=True, null=True, default=None, verbose_name = "SEO ключи к данному Фильтру")
	seo_title = models.TextField(blank=True, null=True, default=None, verbose_name = "SEO тайтл страницы Фильтра")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Фильтры'
		verbose_name_plural = 'Фильтры'

class ProductCart(models.Model):
	title = models.CharField(max_length=100, verbose_name = "Название товара")
	slug = AutoSlugField(populate_from='title')
	description = RichTextField(blank=True, verbose_name = "Подробное описание")
	short_description = RichTextField(blank=True, null=True, default=None, verbose_name = "Краткое описание")
	bottom_description = RichTextField(blank=True, null=True, default=None, verbose_name = "Дополнительное описание")
	pub_date = models.DateField(auto_now_add=True, verbose_name = "Дата публикации")
	mod_date = models.DateField(auto_now=True, verbose_name = "Обновление публикации")
	price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name = "Новая цена")
	discount_price = models.DecimalField(blank=True, null=True, max_digits=18, decimal_places=2, verbose_name = "Старая цена")
	image = models.ImageField(upload_to='products', blank=False, verbose_name = "Главное изображение карточки товара")
	category = TreeManyToManyField(ProductCategory)
	productfilter = models.ManyToManyField(ProductFilter, verbose_name ="Фильтры")
	is_active = models.BooleanField(default=True, verbose_name = "Публикация")
	in_stock = models.BooleanField(default=True, verbose_name = "Наличие товара")
	seo_meta_description = models.TextField(blank=True, null=True, default=None, verbose_name = "SEO Meta описание к данному товару")
	seo_key = models.TextField(blank=True, null=True, default=None, verbose_name = "SEO ключи к данному товару")
	seo_title = models.TextField(blank=True, null=True, default=None, verbose_name = "SEO тайтл страницы товара")
	seo_alt_img = models.TextField(blank=True, null=True, default=None, verbose_name = "SEO ALT Изображения товара")

	@property
	def image_url(self):
		if self.image and hasattr(self.image, 'url'):
			return self.image.url

	def get_review(self):
		return self.reviews_set.filter(published=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

class Images (models.Model):
	product = models.ForeignKey(ProductCart, default=None, null=True, on_delete=models.CASCADE, verbose_name='Дополнительные изображения')
	img = models.ImageField(upload_to='products', blank=True)

	class Meta:
		verbose_name = 'изображения'
		verbose_name_plural = 'Дополнительные Изображения товара'

class ImagesBottom (models.Model):
	product = models.ForeignKey(ProductCart, default=None, null=True, on_delete=models.CASCADE, verbose_name='Изображения в нижней части карточки товара ')
	img = models.ImageField(upload_to='products', blank=True)

	class Meta:
		verbose_name = 'изображения'
		verbose_name_plural = 'Изображения в нижней части карточки товара (Дополнительные)'
