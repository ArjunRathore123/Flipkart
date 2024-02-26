from django.db import models

# Create your models here.

class MyProduct(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to="image")


    def __str__(self):
        return self.name
