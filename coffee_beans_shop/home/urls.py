from django.urls import path

from home import views

urlpatterns = [
    path('',views.home),
    # path("login",views.login),
    # # path("register",views.register,name="register"),
    # # path('register',views.registration),
    
    # path('products/',views.Generics.as_view()),
    # path('product/<int:pk>',views.Generics_pk.as_view()),
    
]