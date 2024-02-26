from django.db import models

# Create your models here.
class Seller(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email = models.EmailField(max_length=255,unique=True,null=True)
    password = models.CharField(max_length=100,)
    mobile_number = models.CharField(max_length=10)
    gender_choice=(('Male','Male'),('Female','Female'),('Other','Other'))
    gender =models.CharField(max_length=6,choices=gender_choice)
    date_of_birth = models.DateField()
    address=models.TextField()
    is_active = models.BooleanField(null=False,default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name