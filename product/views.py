from django.shortcuts import render
from .models import MyProduct
# Create your views here.

def viewproduct(request):
    get_pro = MyProduct.objects.all()
   

    context = {'product':get_pro}
    return render(request,"index.html",context)