from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import GuestRegistrationForm

def register(request):
    if request.method == 'POST':
        form = GuestRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = GuestRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})