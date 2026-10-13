from django import forms
from .models import Registration, ContactMessage, TrainingCourse
from .utils import validate_indian_phone

class RegistrationForm(forms.ModelForm):
    photo = forms.FileField(
        required=False,
        label="Upload Photo",
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*', 'id': 'id_photo'})
    )
    password = forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Create account password', 'id': 'id_password'})
    )
    confirm_password = forms.CharField(
        required=True,
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm account password', 'id': 'id_confirm_password'})
    )

    class Meta:
        model = Registration
        fields = [
            'full_name', 'phone', 'email', 'photo', 'password'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name', 'id': 'id_full_name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10-digit mobile number', 'id': 'id_phone', 'maxlength': '11', 'oninput': "this.value = this.value.replace(/[^0-9+ ]/g, '');"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter active email address', 'id': 'id_email'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        is_valid, result = validate_indian_phone(phone)
        if not is_valid:
            raise forms.ValidationError(result)
        return result

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and len(password) < 4:
            raise forms.ValidationError("Password must be at least 4 characters long.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Password and Confirm Password do not match.")

        return cleaned_data




class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Mobile Number', 'maxlength': '11', 'oninput': "this.value = this.value.replace(/[^0-9+ ]/g, '');"}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Your Message'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        is_valid, result = validate_indian_phone(phone)
        if not is_valid:
            raise forms.ValidationError(result)
        return result



class CertificateSearchForm(forms.Form):
    certificate_number = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Enter Certificate ID (e.g. MT-2026-1001)'
        })
    )
