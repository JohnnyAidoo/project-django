from django.db import models

# Create your models here.
class Users(models.Model):
    userName = models.CharField(max_length=200 , unique=True)
    userContact = models.IntegerField()
    userEmail = models.EmailField(default='null', unique=True)
    userPassword = models.CharField(max_length=200)
    
class Posts(models.Model):
    postImage = models.ImageField(max_length=10000, default='https://www.salonlfc.com/wp-content/uploads/2018/01/image-not-found-1-scaled-1150x647.png')
    postTitle = models.CharField(max_length=200, default='free')
    postPrice = models.IntegerField()
    postCategory = models.CharField(max_length=200,default='others')
