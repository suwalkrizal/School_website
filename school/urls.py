from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


# Create Router
router = DefaultRouter()
router.register(r'banner', BannerViewSet, basename='banner')
router.register(r'about', AboutUsViewSet, basename='about')
router.register(r'blog', BlogPostViewSet, basename='blog')
router.register(r'contact', ContactUsViewSet, basename='contact')


# Define URLs
urlpatterns = [
    path('api/', include(router.urls)),  # Include router-generated URLs
    
]
