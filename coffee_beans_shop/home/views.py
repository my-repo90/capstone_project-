from django.shortcuts import render , redirect
from rest_framework import generics
from . import models
from home.serializers import ProductSerializer
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login

from django.shortcuts import render 
from .forms import CreationForms
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from .models import Product , Purchase
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

def home(request):
    products = Product.objects.all()

    if request.method == "POST":
        product_id = request.POST.get("product_id")
        user_id = request.POST.get("user_id")

        # if product_id:
        #     product = Product.objects.filter(id=product_id).first()
        #     if product and (product.name == request.user)
        if user_id:
            user = User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except:
                    pass

                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass
    return render(request, "home/home.html" , {"products" : products})


# def register(request):
#     if request.method == 'POST':
#         form = CreationForms(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home/login.html')
#     else:
#         form = CreationForms()

#     return render(request, 'registration/login.html', {"form": form})

 def register(request):
#     form = UserCreationForm()
#     return render(request , 'registration/register.html' ,{'form':form})

def login(request):
    form = AuthenticationForm()
    return render(request , 'registration/login.html', {'form':form})