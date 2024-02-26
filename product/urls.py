from django.urls import path
from .views import viewproduct
urlpatterns = [
    
    path('mypro/',viewproduct),

]
