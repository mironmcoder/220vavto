from django.urls import path
from .views import ProductDetailView, CatalogListView, FilterListViews


urlpatterns = [
	path('product/<slug:slug>/', ProductDetailView.as_view() , name="product"),
	path('catalog/<slug:slug>/', CatalogListView.as_view(), name="catalog"),
	path('filter/', FilterListViews.as_view(), name="filter"),
]