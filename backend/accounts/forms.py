from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class GuestRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    guest_type = forms.ChoiceField(choices=[('regular', 'Regular'), ('vip', 'VIP')])
    face_photo = forms.ImageField(required=True, help_text="Upload a clear photo of your face")
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'guest_type', 'face_photo', 'password1', 'password2')