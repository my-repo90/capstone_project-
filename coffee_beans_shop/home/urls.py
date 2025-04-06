from django.urls import path
from django.contrib.auth import views
from home import views


urlpatterns = [
    # path('',views.home , name = 'home'),
    path("register/",views.register),
    path('',views.login),
    path('about/',views.about),
    path('logout/',views.logout),
    path('accounts/profile/',views.profile),

]