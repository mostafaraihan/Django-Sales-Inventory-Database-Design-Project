from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField()
    password = models.CharField(max_length=500)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    otp = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=100)
    username = models.ForeignKey(User, on_delete=models.CASCADE,related_name='categories')  #remove user data (models.CASCADE) use
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places= 2)  #most important (decimal_places) part
    unit = models.CharField(max_length=100)
    username = models.ForeignKey(User, on_delete=models.CASCADE,related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField()
    username = models.ForeignKey(User, on_delete=models.CASCADE,related_name='customers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)