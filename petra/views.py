from django.shortcuts import render
from .models import Product, Cart
from django.contrib.auth.models import User
from .serializers import ProductListSerializer, ProductDetailSerializer, UserCreateSerializer, UserLoginSerializer, CreateProductSerializer, CartSerializer, CartUpdateSerializer
from .permissions import IsBookingOwner
# DRF Imports:
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView,DestroyAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser

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
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'

class Create(CreateAPIView):
    serializer_class = CreateProductSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
class Delete(DestroyAPIView):
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Product.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'

#-----------------------Cart Views-----------------------------

class CartDetails(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = CartSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'cart_id'
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

class CartUpdate(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = CartUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'cart_id'
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    