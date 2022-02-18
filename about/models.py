
from tabnanny import verbose
from django.db import models

# Create your models here.

class Service(models.Model):
    service = models.CharField(max_length=127, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        
    def __str__(self):
        return self.service
    
    
class Interest(models.Model):
    interest = models.CharField(max_length=127, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Interest'
        verbose_name_plural = 'Interests'
        
    def __str__(self):
        return self.interest
    
    
class Education(models.Model):
    title = models.CharField(max_length=127, null=True, blank=True)
    description = models.CharField(max_length=127, null=True, blank=True)
    start_year = models.DateField(null=True, blank=True)
    end_year = models.DateField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        
    def __str__(self):
        return self.title
    
class Experience(models.Model):
    title = models.CharField(max_length=127, null=True, blank=True)
    description = models.CharField(max_length=127, null=True, blank=True)
    start_year = models.DateField(null=True, blank=True)
    end_year = models.DateField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        
    def __str__(self):
        return self.title
    
    
class Blog(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(null=True,blank=True)
    link = models.URLField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='blog/')
    
    def __str__(self):
        return self.title
    
    
class Projects(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(null=True,blank=True)
    link = models.URLField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='blog/')
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
    
    def __str__(self):
        return self.title    
    
    
class Testimonials(models.Model):
    fullname = models.CharField(max_length=255, blank=True, null=True)
    job = models.CharField(max_length=100, null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    image = models.ImageField(upload_to='blog/')
    
    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
    
    def __str__(self):
        return self.fullname 
    
    
class Contact(models.Model):
    fullname = models.CharField(max_length=100,blank=True,null=True)
    email = models.CharField(max_length=100,blank=True,null=True)
    message = models.TextField()
    
    
    def __str__(self):
        return self.fullname
