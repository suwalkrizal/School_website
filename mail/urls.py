from django.urls import path
from .views import contact_us

urlpatterns = [
    path('contactus/', contact_us, name='contact_us'),
]
