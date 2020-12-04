from django.db import models
from apps.product.models import ProductCart


class Order(models.Model):
	name = models.CharField(max_length=50, verbose_name = "Имя")
	phone = models.CharField(max_length=12, verbose_name = "Номер телефона")
	email = models.EmailField(verbose_name = "Email", blank=True, null=True)
	address = models.CharField(max_length=250, verbose_name = "Адрес")
	comment = models.TextField(max_length= 1000, blank=True, null=True, verbose_name = "Комментарий")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False)

	class Meta:
		ordering = ('-created',)
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'

	def __str__(self):
		return 'Order {}'.format(self.id)

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
	product = models.ForeignKey(ProductCart, related_name='order_items', on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return '{}'.format(self.id)

	def get_cost(self):
		return self.price * self.quantity