from django.shortcuts import render
from . models import About, Interest, Service, Education, Experience
from . forms import ContactForm
# Create your views here.

def home(request):
    about = About.objects.get(pk=1)
    services = Service.objects.all()
    interests = Interest.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
    
    context = {
        'about':about,
        'services':services,
        'interests':interests,
        'educations':educations,
        'experiences':experiences,
        'form':form
    }
    return render(request, "index.html", context)