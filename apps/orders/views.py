from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from apps.basket.basket import Basket


def order_create(request):
	basket = Basket(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save()
			for item in basket:
				OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
			basket.clear()
			return render(request, 'orders/created.html', {'order': order})
	else:
		form = OrderCreateForm
	return render(request, 'orders/create.html', {'basket': basket, 'form': form})