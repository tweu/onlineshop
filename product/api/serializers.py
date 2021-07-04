
from product.models import Product
from django.db.models import query
from django.db.models.query import QuerySet
from product.models import Product, Category
from django.http import request
from rest_framework import serializers

class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


