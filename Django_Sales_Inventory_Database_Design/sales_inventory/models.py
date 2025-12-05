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