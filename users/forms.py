from allauth.account.forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import forms

class CustomSignupForm(SignupForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        #iexact means "case-insensitive exact match").
        if email and User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("A user is already registered with this email address.")
        return email
