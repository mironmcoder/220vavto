from .models import ProductCategory, ProductFilter

def category_filter(request):
	cat = ProductCategory.objects.all
	product_filter = ProductFilter.objects.all
	return {'cat':cat, 'product_filter':product_filter}