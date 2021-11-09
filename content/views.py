from django.shortcuts import render
from rest_framework import serializers, viewsets, permissions
from rest_framework.response import Response
from .models import Cv, Post
from .serializers import CvSerializer, PostSerializer, PostBriefSerializer

# Create your views here.


class CvViewSet(viewsets.ViewSet):

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def list(self, request):
        subCv = Cv.objects.all()
        serializers = CvSerializer(subCv, many=True)
        return Response(serializers.data)
    

    def create(self, request):
        serializer = CvSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("success")
        return Response({"error": "invalid field"})


class PostViewSet(viewsets.ViewSet):

    def get_permissions(self):
        # if self.action in ['create']:
        #     permission_classes = [permissions.IsAuthenticated]
        # else:
        permission_classes = []
        return [permission() for permission in permission_classes]

    def list(self, request):
        posts = Post.objects.all()
        serializers = PostBriefSerializer(posts, many=True)
        return Response(serializers.data)
    
    def retrieve(self, request, pk=None):
        try:
            post = Post.objects.get(id=pk)
        except:
            return Response({"error": "post is not in database"})
        
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def create(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("success")
        return Response({"error": "invalid field"})