from django.shortcuts import render , redirect
from rest_framework import generics
from . import models
from home.serializers import ProductSerializer
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login
# # Create your views here.
# def home(request):
#     return render(request ,'home/home.html')

# # class Generics(generics.ListCreateAPIView):
# #     queryset = models.Product.objects.all()
# #     serializer_class = ProductSerializer
   

# # class Generics_pk(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = models.Product.objects.all()
# #     serializer_class = ProductSerializer

# from django.shortcuts import render , redirect
# from accounts.forms import CreationForms
# from accounts.serializers import UserSerializer
# from accounts.models import UserClass
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# # Create your views here.

# def registration(request):
#     return render(request ,'home/register.html')
#     # if request.method == 'POST':
#     #     form = CreationForms(request.POST)
#     # #     # if form.is_valid():
#     # #     #     form.save()
#     # #     #     return redirect('connexion')
        
#     # #     # else:
#     # #     #     form = CreationForms()
#     # #     # # return render(request , 'registration/register.html' , {'form' : form}) 

        
# # def home(request):
# #     return render(request ,'home/home.html')

# #8 Find movie
# @api_view(['GET'])
# def find_user(request):
#     user = UserClass.objects.filter(
#        name = request.data['name'],
#         password = request.data['password'],
#     )
#     serializer = UserSerializer(UserClass, many= True)
#     return Response(serializer.data)

# #9 create new reservation 
# @api_view(['POST'])
# def new_user(request):

#     user= UserClass.objects.get(
#         name = request.data['name'],
#         password = request.data['password'],
#     )
#     guest = UserClass()
#     guest.name = request.data['name']
#     guest.password = request.data['password']
#     guest.save()

#     # reservation = Reservation()
#     # reservation.guest = guest
#     # reservation.movie = movie
#     # reservation.save()

#     return Response(status=status.HTTP_201_CREATED)


from django.shortcuts import render 
from .forms import CreationForms
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from .models import Product , Purchase


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


def register(request):
    if request.method == 'POST':
        form = CreationForms(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home/login.html')
    else:
        form = CreationForms()

    return render(request, 'registration/login.html', {"form": form})