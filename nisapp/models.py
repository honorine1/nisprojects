from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField

# Create your models here.
class Owner(models.Model):
    name = models.TextField(max_length = 20)
    email = models.EmailField(max_length=30)
    phone = models.IntegerField(default=None)
    location =  models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Neighborhood(models.Model):
      nameChoose=(('biryogo','biryogo'),
        ('nyamabuye','nyamabuye'),
        ('nyagatovu','nyagatovu'),
        ('gatenga','gatenga'),
        ('kinyoni','kinyoni'),
        ('kabusunzu','kabusunzu'),
        ('mu kidoge','mu kidoge'),
        ('kabuye','kabuye'),
        ('batsinda','batsinda'),
        ('rutunga','rutunga'),
        ('jabana','jabana'),
     
        
    )
      neighborhoodName=models.CharField(max_length=40,choices=nameChoose)
     
    

class Business(models.Model):
    businessName=  models.CharField(max_length=50)
    businessDesc = models.TextField(max_length = 200)
    image =  models.ImageField(default='',upload_to = 'images/', blank=True) 
    location =  models.CharField(max_length=50)
    businessType = models.CharField(max_length=50)
    owner = models.ForeignKey(Owner)
    neighborhood = models.ForeignKey(Neighborhood)


    def __str__(self):
        return self.businessName

 
class Product(models.Model):
    prodName = models.CharField(max_length=50)
    ProdType = models.CharField(max_length=50)
    prodPrice = models.IntegerField(default=None)
    prodQuantity =models.IntegerField(default=None)
    business = models.ForeignKey(Business)

    def __str__(self):
        return self.prodName

class Profile(models.Model):
    profile_pic =  models.ImageField(default='',upload_to = 'profile_pics/', blank=True) 
    hoodName = models.TextField(max_length = 200)
    bio = models.TextField(max_length = 200)
    location = models.CharField(max_length=50)
    neighbourhood =  models.CharField(max_length=50,null=True)
    contact  = models.IntegerField(default=None)
    general_loc = models.CharField(max_length = 50)
    owner = models.OneToOneField(Owner, on_delete=models.CASCADE,null=True)
    

    def __str__(self):
        return self.bio

class Post(models.Model):
    name =  models.CharField(max_length=50)
    user = models.ForeignKey(User)
    post = HTMLField()
    image =  models.ImageField(upload_to = 'busines_pics/') 

    def __str__(self):
        return self.name

