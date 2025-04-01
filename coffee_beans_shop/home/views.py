from django.shortcuts import render
from rest_framework import generics
from . import models
from home.serializers import ProductSerializer
# Create your views here.
def home(request):
    return render(request ,'home/home.html')

# class Generics(generics.ListCreateAPIView):
#     queryset = models.Product.objects.all()
#     serializer_class = ProductSerializer
   

# class Generics_pk(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Product.objects.all()
#     serializer_class = ProductSerializer