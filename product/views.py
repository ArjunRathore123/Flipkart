from django.shortcuts import render, HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.template import loader
from .models import Product,Category,Brand
# Create your views here.
def products(request):
    get_pro=Product.objects.all()
    context={'product':get_pro}
    print(get_pro)
    return render(request,'productdetails.html',context)

def viewproductdetail(request,pk):
    get_pro=Product.objects.get(id = pk)
    get_color = get_pro.color.all()
    get_size = get_pro.size.all()
    context={
        "getpro":get_pro,
        "getcolor":get_color,
        "getsize":get_size,
       
    }
    print(context)
    
    return render(request,'viewproduct.html',context)

    
def delproductdetail(request,pk):
    get_pro=Product.objects.get(id=pk)
    get_pro.delete()
    
    return HttpResponseRedirect(reverse('product'))

def category(request):
    get_cate=Category.objects.all()
    print(get_cate)
    
    
    return render(request,'category.html',{'category':get_cate})

def subcategory(request,pk):
    getcate=Category.objects.get(id=pk)
    getbrand=Brand.objects.filter(category_id=pk)
    print(getbrand)
    print(getcate)
 
    return render(request,'subcategory.html',{"getbrand":getbrand,"getcate":getcate})

def categorydetail(request,pk):
    getbrand=Brand.objects.get(id=pk)
    getpro=Product.objects.filter(brand=getbrand)
    print(getpro)
    print(getbrand)
    context={"getpro":getpro,
             "getbrand":getbrand}
  
    return render(request,'categorydetail.html',context)

def viewcategorydetail(request,pk):
    get_pro=Product.objects.get(id = pk)
    get_color = get_pro.color.all()
    get_size = get_pro.size.all()
   
    context={
        "getpro":get_pro,
        "getcolor":get_color,
        "getsize":get_size,

        
       
    }
    print(context)
    
    return render(request,'viewcategory.html',context)


    
# def categorys(request,pk):
#     getcategory=Category.objects.get(id=pk)
#     getproduct=Product.objects.filter(category=getcategory).values()
    
#     context={"getproduct":getproduct,
#              "getcate":getcategory}
#     print(context)
#     return render(request,'cate.html',context)