from django.http.response import Http404
from rest_framework.views import APIView
from product.models import Product, Category
from product.api.serializers import ProductModelSerializer
from rest_framework import generics, mixins, viewsets



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

