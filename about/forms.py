from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Contact

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'fullname': forms.TextInput(
                attrs={'id':'name', 'length':'130','style':'margin:5px 10px 5px 10px' ,'placeholder': 'Name'}),
            'email':forms.TextInput(
              attrs={'id':'email','placeholder':'Email'}  
            ),
            'message': forms.Textarea(
                attrs={'id':'message', 'placeholder': 'Message'})
        }