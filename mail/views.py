import threading
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from school.models import ContactUs

# Function to send email in the background
def send_email_background(subject, message, recipient_email):
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [recipient_email],
        fail_silently=False,
    )

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone", "")
        message = request.POST.get("message")

        if not email:  # Ensure email is provided
            return HttpResponse("Email is required.", status=400)

        # Save to database
        contact = ContactUs.objects.create(
            name=name, email=email, phone=phone, message=message
        )

        # Email subject & message
        subject = "Thank You for Contacting Us"
        email_message = f"Hello {name},\n\nWe have received your message:\n\n{message}\n\nWe will get back to you soon!"

        # Run email sending in a background thread
        thread = threading.Thread(target=send_email_background, args=(subject, email_message, email))
        thread.start()

        return HttpResponse("Message sent successfully!")

    return render(request, "contact_form.html")  # Render the contact form page
