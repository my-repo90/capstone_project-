from rest_framework import serializers 
from app.models import UserInfo , ProductInfo , OrderInfo

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta :
        model = UserInfo
        fields = '__all__'

class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta :
        model = ProductInfo
        fields = '__all__'

class OrderInfoSerializer(serializers.ModelSerializer):
    class Meta :
        model = OrderInfo
        fields = '__all__'