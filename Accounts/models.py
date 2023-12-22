from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager


    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    first_name=models.CharField(_("First name"), max_length=100)
    last_name=models.CharField(_("Last Name"), max_length=100)
    mobile_number=models.CharField(_("Mobile Number"),max_length=10)
    date_of_birth = models.DateField(null=True)
    gender_choice=(('Male','Male'),('Female','Female'),('Other','Other'))
    gender =models.CharField(max_length=6,choices=gender_choice)
    address=models.TextField(_("Address"),max_length=200)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    


    
