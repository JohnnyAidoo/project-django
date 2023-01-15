from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Posts
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserSerializer,PostsSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .models import User
# Create your views here.

class PostViewset(viewsets.ModelViewSet):
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
