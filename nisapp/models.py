from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField

# Create your models here.
class Neighborhood(models.Model):
    neighbourhood_name = models.CharField(max_length=30)
    neighbourhood_location = models.CharField(max_length=30)
    occupantsCount = models.IntegerField(default=0)
    admin = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.neighbourhood_name

    @classmethod
    def create_neighborhood(self):
        self.save()

    def delete_neigborhood(self):
        self.delete()

class Business(models.Model):
    businessName=  models.CharField(max_length=50)
    businessDesc = models.TextField(max_length = 200)
    image =  models.ImageField(default='',upload_to = 'images/', blank=True)
    location =  models.CharField(max_length=50)
    businessType = models.CharField(max_length=50)
    neighborhood = models.ForeignKey(Neighborhood)

    def __str__(self):
        return self.businessName

class Product(models.Model):
    prodName = models.CharField(max_length=50)
    image =  models.ImageField(default='',upload_to = 'images/', blank=True)
    ProdType = models.CharField(max_length=50)
    prodPrice = models.IntegerField(default=None)
    prodQuantity =models.IntegerField(default=None)
    business = models.ForeignKey(Business)

    def __str__(self):
        return self.prodName

class Profile(models.Model):
    profile_pic =  models.ImageField(default='',upload_to = 'profile_pics/', blank=True)
    bio = models.TextField(max_length = 200)
    neighbourhood =  models.CharField(max_length=50,null=True)
    contact  = models.IntegerField(default=None)
   
    def __str__(self):
        return self.bio

class Post(models.Model):
    name =  models.CharField(max_length=50)
    user = models.ForeignKey(User)
    post = HTMLField()
    image =  models.ImageField(upload_to = 'busines_pics/')
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
