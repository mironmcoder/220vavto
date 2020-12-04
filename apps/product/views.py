from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductCategory, ProductCart, ProductFilter
from django.views.generic import ListView, DetailView
from apps.basket.forms import BasketAddProductForm
from apps.reviews.forms import ReviewsForm
from django.db.models import Q

class ProductDetailView(DetailView):
	model = ProductCart
	template_name = 'product/product.html'

	def get_context_data(self, **kwargs):
		context = super(ProductDetailView, self).get_context_data(**kwargs)
		context['basket_product_form'] = BasketAddProductForm()
		context['review_form'] = ReviewsForm()
		return context

class CatalogListView(ListView):
	model = ProductCart
	context_object_name = 'product'
	template_name = 'product/catalog.html'

	def get_queryset(self):
		queryset = super(CatalogListView, self).get_queryset()
		category_get_slug = ProductCategory.objects.get(slug=self.kwargs['slug'])
		queryset = queryset.filter(category__pk=category_get_slug.pk)
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		category_get = ProductCategory.objects.get(slug=self.kwargs['slug'])
		catalog_filter = ProductFilter.objects.all
		context['category_get'] = category_get
		context['breadcrumbs'] = category_get.get_ancestors()
		context['catalog_filter'] = catalog_filter
		return context

class FilterListViews(ListView):
	def get_queryset(self):
		name = self.request.GET.getlist("name")
		category_get_slug = ProductCategory.objects.get(slug=name[0])
		queryset = ProductCart.objects.filter(
			Q(productfilter__slug__in=self.request.GET.getlist("slug")) &
			Q(category__pk=category_get_slug.pk)).distinct().values('title', 'price', 'discount_price', 'slug', 'image')
		print(self.request.GET)
		return queryset

	def get(self, request, *args, **kwargs):
		queryset = list(self.get_queryset())
		return JsonResponse({"queryset": queryset}, safe=False)