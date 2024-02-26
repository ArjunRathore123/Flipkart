from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    model=CustomUser
    list_display=('email','first_name','last_name','mobile_number','address','gender','date_of_birth','is_active','is_staff',"date_joined")

    fieldsets=((None,{"fields":('email','password','first_name','last_name','mobile_number','address','gender','date_of_birth',"date_joined")}),
               ("permission",{"fields":('is_staff','is_active')}),
               )
    add_fieldsets=(
        (None,{'classes':("wide",),
               'fields':('email','password','first_name','last_name','mobile_number','address','gender','date_of_birth',"date_joined",'is_staff','is_active')},
        )
    )
    search_fields=('email',)
    ordering=('email',)

admin.site.register(CustomUser,CustomUserAdmin)

