from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.

class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return self.id


class AboutUs(models.Model):
    title = models.CharField(max_length=225)
    content =RichTextField()
    image = models.ImageField(upload_to='about_us/')

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to='blog_images/')
    description = RichTextField(null=True)
    author = models.CharField(max_length=50)
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
