from rest_framework import serializers
from Bookapp.models import Book,User,BookRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model=Book
        fields=["id" ,'title','author','isbn','quantity','genre']
        read_only_fields=['id']

class BookRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model=BookRequest
        fields='__all__'