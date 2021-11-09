from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, viewsets, permissions
from django.contrib.auth import authenticate
from .serializers import LoginSerializer


class UserViewSet(viewsets.ViewSet):
    
    @action(detail= False, methods= ['post'])
    def login(self, request):
        email = request.data.get('email', None)
        password= request.data.get('password', None)
        
        user = authenticate(username= email, password= password)

        if user:
            serializer = LoginSerializer(user)
            return Response(serializer.data)
        return Response({ 'error': 'wrong password or username' })