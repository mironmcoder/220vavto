from django.urls import path
from .views import ReviewsAdd

urlpatterns = [
	path('reviews/', ReviewsAdd.as_view() , name="reviews"),
	]