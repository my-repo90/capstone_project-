from django.db import models

# Create your models here.


class UserInfo(models.Model):
    email = models.EmailField()
    phone = models.IntegerField()
    adress = models.CharField(max_length=50)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return f"last_name:{self.last_name}\nfirst_name:{self.first_name}"

class ProductInfo(models.Model):
    product_name = models.CharField(max_length=25)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"id_product:{self.id_product}\nproduct_name:{self.product_name}"

class OrderInfo(models.Model):
    order_date = models.DateField()
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    def __str__(self):
        return f"order_date: {self.order_date}\nuser: {self.user}"


