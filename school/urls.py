from django.urls import path
from .views import *

urlpatterns = [
    path('banner/', BannerListView.as_view(), name='banner'),
    path('about/', AboutUsListView.as_view(), name='about'),
    path('blog/', BlogPostListView.as_view(), name='blog'),
    path('contact/', ContactUsView.as_view(), name='contact'),
]
