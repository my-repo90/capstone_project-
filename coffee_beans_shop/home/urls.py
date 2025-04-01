from django.urls import path
from home import views

urlpatterns = [
    path("",views.home),
    # path('products/',views.Generics.as_view()),
    # path('product/<int:pk>',views.Generics_pk.as_view()),
    
]