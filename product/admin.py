from django.contrib import admin
<<<<<<< HEAD
from .models import MyProduct

# Register your models here.

admin.site.register(MyProduct)
=======
from .models import Category,Product,Brand,Color,Size
# Register your models here.



# admin.site.register(Product,ProductAdmin)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)

>>>>>>> 94e034a8d2694c6247038fdf68c8ae56cfedbdb7
