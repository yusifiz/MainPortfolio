from django import forms
from django.shortcuts import redirect, render
from . forms import ContactForm
from contact.utils.validators import ValidationError
from django.contrib import messages


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
        
    return render(request, 'index.html', {'form': form})