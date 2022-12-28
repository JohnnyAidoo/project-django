from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets , generics
from .models import Posts, Users
from .serializers import PostsSerializer ,UserSerializer
# Create your views here.

class PostViewset(viewsets.ModelViewSet):
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()


    