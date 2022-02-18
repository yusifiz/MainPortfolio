from django.shortcuts import render
from . models import *
from . forms import ContactForm
# Create your views here.

def home(request):
    services = Service.objects.all()
    interests = Interest.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    blogs = Blog.objects.all()
    projects = Projects.objects.all()
    testimonials = Testimonials.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
    
    context = {
        'services':services,
        'interests':interests,
        'educations':educations,
        'experiences':experiences,
        'blogs':blogs,
        'projects':projects,
        'testimonials':testimonials,
        'form':form
    }
    return render(request, "index.html", context)