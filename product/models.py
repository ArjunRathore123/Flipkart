from django.db import models
<<<<<<< HEAD

# Create your models here.

class MyProduct(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to="image")


    def __str__(self):
        return self.name
=======
from Accounts.models import CustomUser
# Create your models here.

# class MyProduct(models.Model):
#     user=models.OneToOneField(CustomUser,on_delete=models.PROTECT,primary_key=True)
#     product_image = models.ImageField(upload_to="image")
#     product_name = models.CharField(max_length=50)
#     price = models.IntegerField()
#     description=models.TextField()


#     def __str__(self):
#         return self.product_name

class Category(models.Model):
    category_image=models.ImageField(upload_to="image")
    category_name=models.CharField(max_length=50)
   

    def __str__(self):
        return self.category_name

class Brand(models.Model):
   
    brand_image=models.ImageField(upload_to="image")
    brand_name=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.brand_name
    
class Color(models.Model):
    color_name=models.CharField(max_length=50)

    def __str__(self):
        return self.color_name
    
class Size(models.Model):
    size=models.CharField(max_length=20)
    
    def __str__(self):
        return self.size

    
class Product(models.Model):    
    product_image = models.ImageField(upload_to="image")
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    color=models.ManyToManyField(Color)
    size=models.ManyToManyField(Size)
    price = models.IntegerField()
    description=models.TextField()

  
    def __str__(self):
        return self.product_name
>>>>>>> 94e034a8d2694c6247038fdf68c8ae56cfedbdb7
