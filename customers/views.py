from django.shortcuts import render, HttpResponseRedirect,HttpResponse,redirect
from .models import Customer
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# from django.contrib.auth import get_user_model
# User=get_user_model()
# Create your views here.
from Accounts.models import CustomUser
# from .utils import send_email_to_client
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
def home(request):
   # send_email_to_client()
    return render(request,'index.html')

# def send_email(request):
#     send_email_to_client()
#     return HttpResponse("email send successfully please check your")

def slogin(request):
    return render(request,'login.html')

def handlelogin(request):
    if request.method=="POST":
       loginusername=request.POST['loginusername']
       loginpassword=request.POST['loginpassword']
       user= authenticate(username=loginusername,password=loginpassword)
       if user is not None:
           login(request,user)
           messages.success(request,"You are successfully login")
           return redirect('home')
       else:
           messages.error(request,"Invalid Credential")
           return redirect('home')
    return HttpResponse('handlelogin')
    
def handlelogout(request):
    logout(request)
    messages.success(request,"you are successfully logout")
    return redirect('home')

def register(request):
    return render(request,'register.html')

def signup(request):
    if request.method=="POST":
       fname=request.POST['fname']
       lname=request.POST['lname']
       email=request.POST['email']
       mobile_number=request.POST['number']
       address=request.POST['address']
       date=request.POST['birthday']
       gender=request.POST['gender']
       password1=request.POST['password1']
       password2=request.POST['password2']
       
    #    if not email.isalpha():
    #         messages.error(request,"email")
    #         return redirect('home')
       
       if password1 != password2:
            messages.error(request,"Password do not match")
            return redirect('home')
       
       
    
       myuser=CustomUser.objects.create_user(email,password1)
       myuser.first_name=fname
       myuser.last_name=lname
       myuser.address=address
       myuser.date_of_birth=date
       myuser.gender=gender
       myuser.mobile_number=mobile_number
       myuser.save()
       messages.success(request,"Your Flipkart Account has been created successfully")
       return redirect('home')

    else:
        return HttpResponse('404 NOT FOUND')

def customerslist(request):
    get_cus=CustomUser.objects.all()
    return render(request,'customersdetails.html',{'customerdetail':get_cus})

def viewcustomerdetail(request,pk):
    get_cus=CustomUser.objects.get(id = pk)

    return render(request,'view.html',{"getcus":get_cus})

def delcustomerdetail(request,pk):
    get_cus=CustomUser.objects.get(id=pk)
    get_cus.delete()
    
    return HttpResponseRedirect(reverse('customerslist'))

def contactus(request):
    return render(request,'contactus.html')

def send_email(request):
    if request.method=="POST": 
       email=request.POST['email']
       subject=request.POST['subject']
       name=request.POST.get('name','')
       mobile_number=request.POST.get('number','')
       msg=request.POST['message']
       message=f'Name:{name}\nMobile Number:{mobile_number}\n{email}\n{msg}'
       send_mail(subject,message,email,[settings.EMAIL_HOST_USER],fail_silently=True)
    #    email = EmailMessage(
    #        subject,name,mobile_number,message,email,[settings.EMAIL_HOST_USER,],
    #           )
    #    email.send()
       message=f"Hey {name},\nThanks for the enquiry we have received it,\nI am Arjun Rathore. I'm here to welcoming you on behalf of Infograins, I'm a sales director and a founder of Infograins, we will be in touch with you shortly, In a meantime if you have any questions or requirement detail you can revert on this email itself so that based on it we can quickly schedule our discussion or conversation on it.Also, you can schedule a meeting to discuss your specific requirements, here is the calendly link, kindly book your slot as per your convenience, so that we can connect with you to have a more precise conversation regarding your requirement."
       send_mail("Thank you for contact Flipkart",
                 message,
                 settings.EMAIL_HOST_USER,
                 [email],
                 fail_silently=False)
       
       print("------------------------------------------------------")
       print(email)
#
    #    print(subject,message,settings.EMAIL_HOST_USER,[email])
       messages.success(request,"Message sent successfully")
       return render(request,"contactus.html")
    else:
       messages.error(request,"Message not sent ")
       return render(request,"contactus.html")

