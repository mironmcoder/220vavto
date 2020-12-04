from django.db import models
from django.utils import timezone
from apps.product.models import ProductCart

class Basket(models.Model):
	product = models.ForeignKey(ProductCart, default=None, null=True, on_delete=models.SET_NULL)
			