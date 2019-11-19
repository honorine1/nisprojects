from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField

# Create your models here.


class Location(models.Model):
    locationChoose=(
        ('Gatsata','Gatsata'),
        ('Nyamirambo','Nyamirambo'),
        ('Remera','Remera'),
        ('Nyabugogo','Nyabugogo'),
        ('kimironko','kimironko'),
        ('nyarutarama','nyarutarama'),
        ('muhima','muhima'),
        ('kigali','kigali'),
        ('kicukiro','kicukiro'),
        )
    location=models.CharField(max_length=40,choices=locationChoose)
   
 
    def __str__(self):
        return self.location


class Neighborhood(models.Model):
    nameChoose=(('biryogo','biryogo'),
        ('nyamabuye','nyamabuye'),
        ('nyagatovu','nyagatovu'),
        ('gatenga','gatenga'),
        ('kinyoni','kinyoni'),
        ('kabusunzu','kabusunzu'),
        ('karama','karama'),
        ('kabuye','kabuye'),
        ('batsinda','batsinda'),
        ('kagarama','kagarama'),
        ('karuruma','karururma'),
     
        
    )
    neighborhood_name=models.CharField(max_length=40,choices=nameChoose)
   
    location = models.ForeignKey(Location)
    admin =  models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.neighborhood_name

    @classmethod
    def create_neighborhood(self):
        self.save()
      
    @classmethod
    def delete_neighborhood(self):
        self.delete()
    
    @classmethod
    def find_neighborhood(cls,neighborhood_id):
        neighborhood = cls.objects.get(id=neighborhood_id)
        return neighborhood
    
    def update_neighborhood():
        self.update()

    def update_occupants():
        occupants = self.update_occupants.update()
        return occupants

class Business(models.Model):
    businessName=  models.CharField(max_length=50)
    businessDesc = models.TextField(max_length = 200)
    image =  models.ImageField(default='',upload_to = 'images/', blank=True)
    neighborhood = models.ForeignKey(Neighborhood)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    email= models.EmailField(max_length= 30,null=True)
    location = models.ForeignKey(Location)


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

    @classmethod
    def search_product(cls,search_term):
                product= cls.objects.filter(prodName__icontains=search_term)
                return product

class Profile(models.Model):
    profile_pic =  models.ImageField(default='',upload_to = 'profile_pics/', blank=True)
    bio = models.TextField(max_length = 200)
    email=models.CharField(blank=True,max_length=100)
    contact  = models.IntegerField(default=None)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
   
    def __str__(self):
        return self.bio

class Post(models.Model):
    title =  models.CharField(max_length=50)
    post = HTMLField()
    posted_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    neighborhood = models.ForeignKey(Neighborhood)


    def __str__(self):
        return self.name

    @classmethod
    def get_posts(cls):
        
        messages = cls.objects.all()
        return messages
