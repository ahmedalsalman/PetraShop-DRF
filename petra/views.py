from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer
# Create your views here.


class ProductList(ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()


class ProductDetail(RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'
