from django.shortcuts import render
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from Bookapp.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book,User


class CreateUserView(APIView):

    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            return Response({'status':'Created the user'})
        return Response({'error':serializer.errors})


class LoginView(APIView):

    def post(self,request):
        user_id=request.data.user_id
        user=User.Objects.get(pk=user_id)
        if user:
            login(request,user)
            return Response({'status':'User logged in'})
        return Response({'error':'Error in user logging in'})


class LogoutView(APIView):

    def post(self,request):
        logout(request)
        return Response({'Status':'Successfully logged out'})


class CreateBookView(APIView):

    def get(self,request,title_):
        book=Book.objects.get(title=title_)
        serializer=BookSerializer(instance=book)
        return Response({"data":serializer.data})
    
    def post(self,request):
        payload=request.data
        serializer=BookSerializer(data=payload)

        if serializer.is_valid():
            serializer.save()
            return Response({'status':'Created the book'},status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def put(self,request):
        return
    
    def delete(self,request):
        return
    

class RequestBookView(APIView):

    def get(self,request,id):
        query=BookRequest.objects.get(pk=id)
        serializer=BookRequestSerializer(instance=query)
        return Response({'data':serializer.data})
        
    def post(self,request):
        payload=request.data
        serializer=BookRequestSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"Book created successfully"})
        return Response({"error":serializer.errors})

