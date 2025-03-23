from django.shortcuts import render
from app.models import UserInfo , ProductInfo , OrderInfo
from rest_framework import generics
from rest_framework import mixins
from app.serializers import UserInfoSerializer , OrderInfoSerializer , ProductInfoSerializer
from rest_framework import filters

#for users    
class User(generics.ListCreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

class User_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
#for products :
class Product(generics.ListCreateAPIView):
    queryset = ProductInfo.objects.all()
    serializer_class = ProductInfoSerializer
   
class Product_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductInfo.objects.all()
    serializer_class = ProductInfoSerializer


class ProductListView(generics.ListAPIView):
    queryset = ProductInfo.objects.all()
    serializer_class = ProductInfoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['product_name']

#for orders
class Order(generics.ListCreateAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderInfoSerializer

class Order_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderInfoSerializer