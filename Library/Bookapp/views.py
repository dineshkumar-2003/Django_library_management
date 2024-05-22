from django.shortcuts import render
from django.contrib.auth import logout, login , authenticate
from rest_framework import permissions 
from rest_framework.authentication import BasicAuthentication
from Bookapp.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book,User


class CreateUserView(APIView):

    permission_classes=[permissions.AllowAny]

    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            return Response({'status':'Created the user'})
        return Response({'error':serializer.errors})


class LoginView(APIView):

    permission_classes=[permissions.AllowAny]

    def post(self,request):
        user_name=request.data.user_name
        password=request.data.password
        user=authenticate(request=request,username=user_name,password=password)
        if user:
            login(request,user)
            return Response({'status':'User logged in'})
        return Response({'error':'Error in user logging in'})


class LogoutView(APIView):

    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[BasicAuthentication]

    def post(self,request):
        logout(request)
        return Response({'Status':'Successfully logged out'})


class CreateBookView(APIView):

    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[BasicAuthentication]

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
        return Response({'Put':'Success'})
    
    def delete(self,request):
        return Response({'Delete':'Success'})
    

class RequestBookView(APIView):

    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[BasicAuthentication]
    
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

