from typing import Protocol
from product.views import ProductDetailView, ProductListView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', ProductListView.as_view(), name = 'product_list'),
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('api/', include('product.api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)