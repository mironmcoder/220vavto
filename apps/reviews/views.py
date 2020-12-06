from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic.base import View
from apps.product.models import ProductCart
from .models import Reviews
from .forms import ReviewsForm


class ReviewsAdd(View):
	def post(self, request):
		if request.method == 'POST':
			form = ReviewsForm(request.POST)
			if form.is_valid():
				form = form.save(commit=False)
				product_id = request.POST['product']
				form.product = ProductCart.objects.get(pk=product_id)
				if(int(request.POST.get('parent')) > 0):
					form.parent_id = int(request.POST.get('parent'))
				form.save()
				return HttpResponse(status=201)
			else:
				return HttpResponse(status=403)

			


