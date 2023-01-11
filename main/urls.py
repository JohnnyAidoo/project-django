from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from .views import RegisterAPI
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]


router = DefaultRouter()
router.register(r'post',views.PostViewset, basename='post')
router.register(r'users', views.UserViewset, basename='users')

urlpatterns += router.urls
