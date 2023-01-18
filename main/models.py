from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Posts(models.Model):
    postImage = models.ImageField(max_length=10000, default='noImg.png')
    postTitle = models.CharField(max_length=200, default='free')
    postPrice = models.IntegerField()
    postCategory = models.CharField(max_length=200,default='others')

