from django.shortcuts import render

# Create your views here.
from rest_framework import routers, filters, viewsets, status
from .models import *
from .serializers import *

from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

import threading
from django.core.mail import send_mail
from django.conf import settings
# from django.http import HttpResponse
from rest_framework.response import Response


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    filter_backends = (SearchFilter,DjangoFilterBackend)
    pagination_class=PageNumberPagination
    search_fields = ('id',)

class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    filter_backends = (SearchFilter,DjangoFilterBackend)
    pagination_class=PageNumberPagination
    search_fields = ('title',)

# Blog Post ViewSet
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    filter_backends = (SearchFilter,DjangoFilterBackend)
    pagination_class=PageNumberPagination
    search_fields = ('title', 'author__email',)

# Function to send email in the background
def send_email_background(subject, message, recipient_email):
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [recipient_email],
        fail_silently=False,
    )
    
# Contact ViewSet
class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    filter_backends = (SearchFilter,DjangoFilterBackend)
    pagination_class=PageNumberPagination
    search_fields = ('name', 'email',)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()

            # Email subject & message
            subject = "Thank You for Contacting Us"
            email_message = f"Hello {contact.name},\n\nWe have received your message:\n\n{contact.message}\n\nWe will get back to you soon!"

            # Send email in the background
            thread = threading.Thread(target=send_email_background, args=(subject, email_message, contact.email))
            thread.start()

            return Response({"message": "Message sent successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




