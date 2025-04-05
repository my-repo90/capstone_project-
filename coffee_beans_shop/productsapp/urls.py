from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('',views.home),
    path('product<int:pk>/' , views.pk),
    path('products/' , views.rest),
    path('pro/',views.no_rest),



]