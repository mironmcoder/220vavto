from django.db import models
from apps.product.models import ProductCart
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Reviews(MPTTModel):
	username = models.CharField(max_length=100, verbose_name="Имя пользоватиля")
	email = models.EmailField(max_length=50)
	comment = models.TextField(max_length=2000, verbose_name="Комментарий пользователя")
	videourl = models.CharField(max_length=400, blank=True, null=True, verbose_name="Ссылка на видео с ютуба")
	product = models.ForeignKey(ProductCart, on_delete=models.CASCADE, verbose_name="продукт на который написан отзыв")
	parent = models.ForeignKey('self', verbose_name="Ответ на отзыв", on_delete=models.CASCADE, related_name='children', blank=True, null=True)
	created = models.DateField(auto_now_add=True, verbose_name="Дата публикации")
	published = models.BooleanField(default=False, verbose_name="Опубликовать комментарий")

	class Meta:
		verbose_name = "Отзыв"
		verbose_name_plural = "Отзывы"

	def __str__(self):
		return self.username

class ReviewsImages(models.Model):
	review = models.ForeignKey(Reviews, default=None, null=True, on_delete=models.CASCADE, verbose_name="Вложенные фотографии")
	images = models.ImageField(upload_to='reviews', blank=True)