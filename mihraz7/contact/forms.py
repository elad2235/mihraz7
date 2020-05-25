from django import forms
from .models import contact

class contactForm(forms.ModelForm):
    date = forms.DateTimeField(required = False)
    
    class Meta:
        model = contact
        fields = ("Name", "Email", "Subject", "Message")