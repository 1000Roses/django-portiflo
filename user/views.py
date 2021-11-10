from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, viewsets, permissions
from django.contrib.auth import authenticate
from .serializers import LoginSerializer

from django.conf import settings
from django.core.mail import send_mail
import re
 
# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
  
def check_email(email):
 
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        return True
 
    else:
        return False

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

    @action(detail=False, methods=['post'])
    def send_email(self, request):
        from_email = request.data.get("from_email", None)
        text       = request.data.get("text", None)

        if from_email and text and check_email(from_email):
            
            subject = 'PORTIFLO MAIL'
            message = f'From email customer {from_email}, content: {text}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_HOST_USER, ]
            send_mail( subject, message, email_from, recipient_list )

            return Response('sent')

        return Response({ 'error': 'invalid field' })