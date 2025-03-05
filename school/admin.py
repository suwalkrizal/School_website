from django.contrib import admin
from .models import *



@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')  
    search_fields = ('id',)  


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'image')
    search_fields = ('title',)
    list_filter = ('title',)


# Register BlogPost Model
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'description','author', 'publish_date', 'status', 'content')
    search_fields = ('title', 'author__email')
    list_filter = ('status', 'author')

# Register Contact Model
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'message')
    search_fields = ('name', 'email')
    list_filter = ('email',) 
    

