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
                attrs={'id':'name','style':'margin:5px 0px; width:100%;background:transparent ;outline:none; border: 1px solid rgba(0,0,0,.1)','placeholder': 'Name'}),
            'email':forms.TextInput(
              attrs={'id':'email','style':'margin:5px 0px 10px 0px;background:transparent ; width:100%; outline:none; border: 1px solid rgba(0,0,0,.1)' ,'placeholder':'Email'}  
            ),
            'message': forms.Textarea(
                attrs={'id':'message', 'placeholder': 'Message'})
        }