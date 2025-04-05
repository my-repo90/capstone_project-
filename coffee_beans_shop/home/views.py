from django.shortcuts import render , redirect
from . import models
from productsapp import models
from django.shortcuts import render 
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.template import RequestContext
from django.template import loader
from django.http import HttpResponse

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
            return redirect('home/home.html')
    else:
        form = AuthenticationForm()
    args = {'form': form}
    return render(request, 'home/home.html')


def about(request):
    return render(request,'home/aboutus.html')


def logout(request):
    logout(request)
    return redirect('home')

# def home(request):
#   products = models.Product.objects.all().values()
#   template = loader.get_template('home/home.html')
#   context = {
#     'products': products,
#   }
#   return HttpResponse(template.render(context, request))
@login_required
def profile(request):
    return render(request,'home/profile.html')
