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
        ('Kimironko','Kimironko'),
        ('Nyarutarama','Nyarutarama'),
        ('Muhima','Muhima'),
        ('Kigali','Kigali'),
        ('Kicukiro','Kicukiro'),
        ('Gikondo','Gikondo'),
        ('Gacuriro','Gacuriro'),
        ('Kacyiru','Kacyiru'),
        ('Kibagabaga','Kibagabaga'),
        ('Gisozi','Gisozi'),
        ('Kabeza','Kabeza')
        )
    location=models.CharField(max_length=40,choices=locationChoose)
    admin =  models.ForeignKey(User, on_delete=models.CASCADE,null=True)
   
 
    def __str__(self):
        return self.location

    @classmethod
    def search_by_location(cls,search_term):
                location= cls.objects.filter(location__icontains=search_term)
                return location



class Neighborhood(models.Model):
    nameChoose=(('Biryogo','Biryogo'),
        ('Nyamabuye','Nyamabuye'),
        ('Nyagatovu','Nyagatovu'),
        ('Gatenga','Gatenga'),
        ('Kinyoni','Kinyoni'),
        ('Kabusunzu','Kabusunzu'),
        ('Karama','Karama'),
        ('Kabuye','Kabuye'),
        ('Batsinda','Batsinda'),
        ('Kagarama','Kagarama'),
        ('Karuruma','Karururma'),
        ('Kinamba','Kinamba'),
        ('Kacyiru1','Kacyiru1'),
        ('Kigarama','Kigarama'),
        ('Kabeza2','Kabeza2'),
        ('Kibagabaga1','Kibagabaga1'),
        ('Kagugu','Kagugu'),
        ('Nyakabanda','Nyakabanda'),
        ('Niboye','Niboye'),
        ('Kinyinya','Kinyinya')
     
        
    )
    neighborhood_name=models.CharField(max_length=40,choices=nameChoose)
   
    location = models.ForeignKey(Location)
    # admin = models.ManyToManyField(User)
    # admin =  models.OneToOneField(User, on_delete=models.CASCADE)
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
    # def search_by_neighborhood_name(cls,search_term):
    #     neighborhoods = cls.objects.filter(business__neighborhood_name__icontains=search_term)
        # activities = cls.objects.filter(loca__location_name__contains=search_term)
        # return neighborhoods

class Join(models.Model):
    user=models.OneToOneField(User)
    neighborhood = models.ForeignKey(Neighborhood)

class Business(models.Model):
    businessName=  models.CharField(max_length=50)
    businessDesc = models.TextField(max_length = 200)
    image =  models.ImageField(upload_to = 'images/', blank=True)
    neighborhood = models.ForeignKey(Neighborhood)
    admin =  models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    # user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    email= models.EmailField(max_length= 30,null=True)
    location = models.ForeignKey(Location)

    
    def __str__(self):
        return self.businessName

    
    @classmethod
    def filter_by_business(cls, id):
      product= Product.objects.filter(business_id=id)
      return product

    @classmethod
    def search_by_businessName(cls,search_term):
                product= cls.objects.filter(businessName__icontains=search_term)
                return product

class Product(models.Model):
    prodName = models.CharField(max_length=50)
    image =  models.ImageField(default='',upload_to = 'images/', blank=True)
    ProdType = models.CharField(max_length=50)
    prodPrice = models.IntegerField(default=None)
    prodQuantity =models.IntegerField(default=None)
    business = models.ForeignKey(Business)
    admin =  models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    

    def __str__(self):
        return self.prodName

    @classmethod
    def get_all_products(cls):
        products = cls.objects.all()
        return products
   

    @classmethod
    def search_by_prodName(cls,search_term):
                product= cls.objects.filter(prodName__icontains=search_term)
                return product

class Profile(models.Model):
    profile_pic =  models.ImageField(default='',upload_to = 'profile_pics/', blank=True)
    bio = models.TextField(max_length = 200)
    email=models.CharField(blank=True,max_length=100)
    contact  = models.IntegerField(default=None)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)

    
   
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
