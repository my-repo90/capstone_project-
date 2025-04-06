from django.urls import path
from django.contrib.auth import views
from home import views


urlpatterns = [
    # path('',views.home , name = 'home'),
    path("register/",views.register, name='register'),
    path('login/',views.login,name='login'),
    path('about/',views.about,name='about'),
    path('logout/',views.logout, name='logout'),
    path('accounts/profile/',views.profile , name='profile'),

]