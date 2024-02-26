from django.urls import path
<<<<<<< HEAD
from .views import viewproduct
urlpatterns = [
    
    path('mypro/',viewproduct),

]
=======
from .views import products,viewproductdetail,delproductdetail,category,subcategory,categorydetail,viewcategorydetail
urlpatterns = [
    path('product/',products,name='product'),
    path('viewproduct/<int:pk>/',viewproductdetail,name='viewproduct'),
    path('deleteproduct/<int:pk>/delete/',delproductdetail,name='deleteproduct'),
    path('category/',category,name='category'),
    path('subcategory/<int:pk>',subcategory,name="subcategory"),
    path('categorydetail/<int:pk>',categorydetail,name="categorydetail"),
    path('viewcategory/<int:pk>/',viewcategorydetail,name="viewcategory")

    # path('cate/<int:pk>',categorys)
  
    
]
>>>>>>> 94e034a8d2694c6247038fdf68c8ae56cfedbdb7
