from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin
from mptt.models import TreeManyToManyField
from django.utils.safestring import mark_safe

# Register your models here.
class GalleryInline(admin.TabularInline):
	fk_name = 'product'
	model = Images

class GalleryInlineBottom(admin.TabularInline):
	fk_name = 'product'
	model = ImagesBottom

@admin.register(ProductCart)
class ProductAdmin(admin.ModelAdmin):
	inlines = [GalleryInline, GalleryInlineBottom]
	list_display = ['get_thumb', 'title', 'price', 'discount_price', 'is_active', 'in_stock', 'pub_date', 'mod_date']
	list_display_links = ['title']
	list_filter = ['is_active', 'in_stock', 'productfilter', 'category']

	def get_thumb(self, obj):
		return mark_safe(f'<img style="width: 70px; height: 70px;" src="{obj.image.url}"/>')

	get_thumb.short_description = "Изображение"

class ProductFilterAdmin(admin.ModelAdmin):
	pass



admin.site.register(ProductFilter, ProductFilterAdmin)
admin.site.register(ProductCategory, MPTTModelAdmin)


