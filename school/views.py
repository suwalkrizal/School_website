from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from django.core.mail import send_mail
from django.conf import settings
import threading

from .models import *
from .serializers import *


class BannerListView(APIView):
    def get(self, request):
        queryset = Banner.objects.all()
        paginator = PageNumberPagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = BannerSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)


class AboutUsListView(APIView):
    def get(self, request):
        queryset = AboutUs.objects.all()
        paginator = PageNumberPagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = AboutUsSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)


class BlogPostListView(APIView):
    def get(self, request):
        queryset = BlogPost.objects.all()
        paginator = PageNumberPagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = BlogPostSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)


# Function to send email in the background
def send_email_background(subject, message, recipient_email):
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [recipient_email],
        fail_silently=False,
    )


class ContactUsView(APIView):
    def get(self, request):
        queryset = ContactUs.objects.all()
        paginator = PageNumberPagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = ContactUsSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = ContactUsSerializer(data=request.data)
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
