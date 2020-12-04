"""vavto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexListView.as_view(), name = "index"),
    path('', include('apps.product.urls')),
    path('', include(('apps.basket.urls', 'basket'), namespace='basket')),
    path('orders/', include(('apps.orders.urls', 'order'), namespace='order')),
    path('', include('apps.reviews.urls')),
    path('contact/', views.contact, name="contact"),
    path('contact/error/', views.contact_error, name="error"),
    path('contact/thanks/', views.contact_thanks, name="thanks"),
    path('help/', views.help, name="help"),
    path('delivery/', views.delivery, name="delivery"),
    path('captcha/', include('captcha.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
