from django.shortcuts import render
from .models import Product
from django.contrib.auth.models import User
from .serializers import ProductListSerializer, ProductDetailSerializer, UserCreateSerializer, UserLoginSerializer, CreateProductSerializer

# DRF Imports: (👍 on organizing imports)
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView,DestroyAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser

# a convention is to keep two empty lines above a class definition in Python


class Register(CreateAPIView):
    serializer_class = UserCreateSerializer


class ProductList(ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()


class ProductDetail(RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'


class Update(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser] # product owner can't update their own product?
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'


class Create(CreateAPIView):
    serializer_class = CreateProductSerializer # can't add a description to a product when creating/updating it?
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class Delete(DestroyAPIView):
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminUser] #creator of the product can't delete their own product off the market?
    queryset = Product.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'
