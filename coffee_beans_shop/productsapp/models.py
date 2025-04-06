from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.PositiveIntegerField()
    # def __str__(self):
    #     return self.name + " " + self.price + " " + self.stock

class Purchase(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    purchase_date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.customer + " " + self.purchase_date + " " + self.product