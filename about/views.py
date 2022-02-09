from django.shortcuts import render
from . models import About, Interest, Service, Education, Experience
# Create your views here.

def home(request):
    about = About.objects.get(pk=1)
    services = Service.objects.all()
    interests = Interest.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    
    context = {
        'about':about,
        'services':services,
        'interests':interests,
        'educations':educations,
        'experiences':experiences
    }
    return render(request, "index.html", context)