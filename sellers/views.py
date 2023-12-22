from django.shortcuts import render,HttpResponseRedirect
from .models import Seller
from django.urls import reverse
# Create your views here.
def sellerlogin(request):
    return render(request,'sellerlogin.html')

def sellerindex(request):
    return render(request,"sellerindex.html")

def sellerreg(request):
    return render(request,"sellregister.html")

def sellerslist(request):
    get_data=Seller.objects.all()
    return render(request,'sellersdetails.html',{'sellerdetail':get_data})

def viewsell(request,pk):
    get_sell=Seller.objects.get(id=pk)
    print(get_sell)
    return render(request,'viewseller.html',{'getsell':get_sell})

def deletesell(request,pk):
    del_sell=Seller.objects.get(id=pk)
    del_sell.delete()
    return HttpResponseRedirect(reverse('sellerslist'))
