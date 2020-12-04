from django.contrib import admin
from .models import *

class ReviewsAdmin(admin.ModelAdmin):
	list_display = ['username', 'email', 'product', 'created', 'published']

admin.site.register(Reviews, ReviewsAdmin)

# Register your models here.
