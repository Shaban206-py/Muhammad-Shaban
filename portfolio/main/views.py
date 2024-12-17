from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.core.exceptions import ValidationError
import logging
from .forms import ContactForm  # This is the form we will create in the next step
from .models import Project

# Create a logger instance
logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def projects(request):
    return render(request, 'main/projects.html')

def contact(request):
    if request.method == 'POST':
        # Using the form for validation
        form = ContactForm(request.POST)
        
        if form.is_valid():
            # Get cleaned data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Log the received form data
            logger.info(f"Received message from {name} ({email}) - Subject: {subject}")

            # Prepare email content
            email_subject = f"Message from {name} - {subject}"
            email_body = f"""
            Name: {name}
            Email: {email}
            Phone: {phone}
            Subject: {subject}
            Message: {message}
            """
            
            try:
                # Send email
                send_mail(
                    email_subject,  # Subject line
                    email_body,     # Message body
                    email,          # From email
                    [settings.EMAIL_HOST_USER],  # To email (your email)
                    fail_silently=False,  # Ensure errors are raised on failure
                )
                logger.info(f"Email successfully sent to {settings.EMAIL_HOST_USER}")
                return render(request, 'main/contact.html', {'form': form, 'message': 'Your message has been sent successfully!'})
            
            except Exception as e:
                # Log the error and show the user a friendly message
                logger.error(f"Failed to send email: {e}")
                return render(request, 'main/contact.html', {'form': form, 'message': 'There was an error sending your message. Please try again later.'})
        
        else:
            # If the form is not valid, display errors
            logger.warning(f"Form validation failed: {form.errors}")
            return render(request, 'main/contact.html', {'form': form, 'message': 'Please fill out all fields correctly.'})
    
    else:
        # Display the form when it's not a POST request
        form = ContactForm()
        return render(request, 'main/contact.html', {'form': form})

def projects(request):
    # Query the Project model for all projects
    projects = Project.objects.all()
    
    # Pass the projects data to the template
    return render(request, 'main/projects.html', {'projects': projects})