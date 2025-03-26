from django.db import models

# Create your models here.
class UserInfo(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    #location
    password = models.CharField(max_length=30)

