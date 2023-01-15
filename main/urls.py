from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('login/' , TokenObtainPairView.as_view(), name ="obtain_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    ]


router = DefaultRouter()
router.register(r'post',views.PostViewset, basename='post')
router.register(r'users', views.UserViewset, basename='users')

urlpatterns += router.urls
