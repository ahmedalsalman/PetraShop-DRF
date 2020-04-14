from django.shortcuts import render
from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer, UserCreateSerializer, UserLoginSerializer

# DRF Imports:
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


class Register(CreateAPIView):
    serializer_class = UserCreateSerializer


class Login(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)


class ProductList(ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()


class ProductDetail(RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'

# class CreateView(CreateAPIView):
#     serializer_class = ProductListSerializer

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)