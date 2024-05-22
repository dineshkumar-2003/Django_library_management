from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    phone_number = models.CharField(max_length=11)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age=models.PositiveIntegerField(null=True,blank=True)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.first_name
    

class Book(models.Model):

    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    isbn=models.CharField(max_length=13)
    genre=models.CharField(max_length=20,blank=True,null=True)
    quantity=models.PositiveIntegerField()

    def __str__(self):
        return self.title


class BookRequest(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.book}'




    
