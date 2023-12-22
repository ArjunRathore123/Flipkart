from django.db import models


# Create your models here.

class Customer(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email = models.EmailField(max_length=255,unique=True,null=True)
    password = models.CharField(max_length=100,)
    mobile_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    gender_choice=(('M','Male'),('F','Female'),('O','Other'))
    gender =models.CharField(max_length=1,choices=gender_choice)
    address=models.TextField()
    is_active = models.BooleanField(null=False,default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
    

    
