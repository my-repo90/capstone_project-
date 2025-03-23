from django.contrib import admin
from .models import UserInfo , ProductInfo , OrderInfo
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(ProductInfo)
admin.site.register(OrderInfo)
