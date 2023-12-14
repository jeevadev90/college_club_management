from django.db import models

from django.utils import timezone
# Create your models here.
# Create your models here.
import datetime
import os
from django.core.validators import RegexValidator


def getFilename(request,filename):
    now_time =datetime.datetime.now().strftime("%Y%n%d%H:%M:%S")
    new_filename = "%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class Club(models.Model):
    club_name = models.CharField(max_length=50, null=False,blank=False)
    logo = models.ImageField(upload_to=getFilename,null=True,blank=True)
    incharge_name = models.CharField(max_length=50,null=False,blank=False)
    organizer_name = models.CharField(max_length=50,null=False,blank=False)
    boys_name = models.CharField(max_length=50,null=False,blank=False)
    girls_name = models.CharField(max_length=50,null=False,blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.club_name}'
    
class Department(models.Model):
    name =models.CharField(max_length=100,null=False,blank=False)
    

    def __str__(self):
        return f'{self.name}'
    
class Club_members(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50,null=False,blank=False)
    phone_number = models.CharField(
        max_length=13,  
        validators=[
            RegexValidator(
                regex=r'^\d{9,10}$',  # Customize the regex pattern for your needs
                message="Phone number must be entered in the format: '1234567890'."
            ),
        ],
        blank=True,     
        null=True,      
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return f'{self.student_name} - {self.phone_number}'
    
class Events(models.Model):
    event_name= models.CharField(max_length=500, null=True, blank=True)
    event_organizer = models.CharField(max_length=50, null=True, blank=True)
    event_date = models.DateField( null=True, blank=True)
   

    def __str__(self):
       return f'{self.event_name} '
    
class Index_content(models.Model):
    texts = models.TextField(max_length=2000, null=True, blank=True)
    imaages = models.ImageField(upload_to=getFilename,null=True, blank=True)    

    def __str__(self):
        return f'{self.imaages}'
    

class Gallery(models.Model):
    clbs = models.ForeignKey(Club,on_delete=models.CASCADE)
    galimage = models.ImageField(upload_to=getFilename, null=False, blank=False)

    def __star__(self):
        return f'{self.galimage}'


