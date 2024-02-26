from django.db import models

# Create your models here.
class Superadmin(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email = models.EmailField(max_length=255,unique=True,null=True)
    password = models.CharField(max_length=100,)
    mobile_number = models.CharField(max_length=10)
    gender_choice=(('Male','Male'),('Female','Female'),('Other','Other'))
    Gender =models.CharField(max_length=6,choices=gender_choice)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(null=False,default=True)