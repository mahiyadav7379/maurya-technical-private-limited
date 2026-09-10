from django import forms
from .models import Registration, ContactMessage

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
            'full_name', 'email', 'phone', 'whatsapp_number', 
            'college', 'branch', 'year_of_study', 
            'course_interested', 'training_type', 'city'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter mobile number'}),
            'whatsapp_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'WhatsApp number'}),
            'college': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'College / Institute Name'}),
            'branch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Branch / Course (e.g., CS, IT, BCA)'}),
            'year_of_study': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Year of Study (e.g., 3rd Year)'}),
            'course_interested': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Interested Training Course'}),
            'training_type': forms.Select(attrs={'class': 'form-select'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your City'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Mobile Number'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Your Message'}),
        }


class CertificateSearchForm(forms.Form):
    certificate_number = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Enter Certificate ID (e.g. MT-2026-1001)'
        })
    )
