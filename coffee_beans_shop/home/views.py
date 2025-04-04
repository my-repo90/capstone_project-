from django.shortcuts import render , redirect
from rest_framework import generics
from . import models

from django.contrib.auth.decorators import login_required, permission_required
from django.http.response import JsonResponse 
from productsapp import models
from django.shortcuts import render 
from .forms import CreationForms
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.template import RequestContext
from django.template import loader
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# def home(request):
#     products = Product.objects.all()

#     if request.method == "POST":
#         product_id = request.POST.get("product_id")
#         user_id = request.POST.get("user_id")

#         # if product_id:
#         #     product = Product.objects.filter(id=product_id).first()
#         #     if product and (product.name == request.user)
#         if user_id:
#             user = User.objects.filter(id=user_id).first()
#             if user and request.user.is_staff:
#                 try:
#                     group = Group.objects.get(name='default')
#                     group.user_set.remove(user)
#                 except:
#                     pass

#                 try:
#                     group = Group.objects.get(name='mod')
#                     group.user_set.remove(user)
#                 except:
#                     pass
#     return render(request, "home/home.html" , {"products" : products})


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
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(
                request,
                username = username,
                password = password
            )
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    args = {'form': form}
    return render(request, 'registration/register.html', args)
def login(request):
    if request.method =='POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(
                request,
                username = username,
                password = password
            )
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    args = {'form': form}
    return render(request, 'home/home.html')


def about(request):
    return render(request,'home/aboutus.html')


def logout(request):
    logout(request)
    return redirect('home')

def home(request):
  products = models.Product.objects.all().values()
  template = loader.get_template('home/home.html')
  context = {
    'products': products,
  }
  return HttpResponse(template.render(context, request))

