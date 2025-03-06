from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.

class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return f"Banner: {self.image.name}" if self.image else "Banner: No Image"



class AboutUs(models.Model):
    title = models.CharField(max_length=225)
    content =RichTextField()
    image = models.ImageField(upload_to='about_us/', blank=True, null=True)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    description = RichTextField(null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    content =RichTextField()

    def __str__(self):
        return self.title


# Contact Model
class ContactUs(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    phone = models.CharField(max_length=225, blank=True, null=True)  # Phone is optional
    message = RichTextField()

    def __str__(self):
        return self.name
