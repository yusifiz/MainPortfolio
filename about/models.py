from django.db import models

# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=63, null=True, blank=True)
    address = models.CharField(max_length=63, null=True, blank=True)
    study = models.CharField(max_length=63, null=True, blank=True)
    degree = models.CharField(max_length=63, null=True, blank=True)
    mail = models.EmailField(max_length=63, null=True, blank=True)
    phone = models.CharField(max_length=63, null=True, blank=True)
    
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
        
    def __str__(self):
        return self.name
    

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