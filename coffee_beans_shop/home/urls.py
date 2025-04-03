from django.urls import path
from django.contrib.auth import views
from home import views

urlpatterns = [
    path('',views.home),
    # path("",views.login),
    
   
]