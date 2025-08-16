from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterSignupForm
from .models import Subscriber

def newsletter_signup(request):
    if request.method == "POST":
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            # Prevent duplicates
            if not Subscriber.objects.filter(email=email).exists():
                form.save()
                messages.success(request, "You have successfully subscribed to our newsletter!")
            else:
                messages.info(request, "This email is already subscribed.")
            return redirect("newsletter:newsletter_signup")
    else:
        form = NewsletterSignupForm()
    
    return render(request, "newsletter/newsletter_signup.html", {"form": form})
