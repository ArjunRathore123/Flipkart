from django.contrib import admin
from .models import Category,Product,Brand,Color,Size
# Register your models here.



# admin.site.register(Product,ProductAdmin)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)

