from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('product<int:pk>/' , views.pk),
    path('products/' , views.rest),
    # path('pro/',views.no_rest),
    path('product/<int:product_id>/',views.prodInfos, name='product_details'),

]