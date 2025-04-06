from django.shortcuts import render
from django.shortcuts import render , redirect
from rest_framework import generics
from . import models
from .serializers import ProductSerializer , PurchaseSerializer
from django.contrib.auth.decorators import login_required, permission_required
from django.http.response import JsonResponse 

from django.shortcuts import render 

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from .models import Product , Purchase
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.template import RequestContext
from django.template import loader
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

@api_view(['GET', 'POST'])
def rest(request):
    #GET
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products , many= True)
        return Response(serializer.data)
    
    #POST 
    elif request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status.HTTP_201_CREATED)
        return Response(serializer.data , status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def pk(request , pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    #GET

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
     
    #PUT 
    elif request.method == 'PUT':
        serializer = ProductSerializer(product , data = request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.error_messages , status.HTTP_400_BAD_REQUEST)
    
    #DELETE
    if request.method == 'DELETE':
        product.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    

def no_rest(request):
    products = [
        {
            'name' : "PRODUCT1",
            'price' : 12365,
            'stock' : 1500,
                    
        }
        ,
        { 
            'name' : "PRODUCT2",
            'price' : 88765,
            'stock' : 22000,
                    
        }
]

    
    return JsonResponse(products , safe=False)

def home(request):
    products = Product.objects.all()
    return render(request , 'templates/productsapp/products.html' , {'products':products})
