from django import forms
from .models import Subscriber

class NewsletterSignupForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ["email"]
