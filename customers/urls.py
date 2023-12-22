from django.urls import path
from .views import home, slogin, register,customerslist,viewcustomerdetail,delcustomerdetail,signup,handlelogin,handlelogout,send_email,contactus


urlpatterns = [
    path('',home,name='home'),
    path('login/',slogin,name='login'),
    path('login',handlelogin,name='login'),
    path('logout',handlelogout,name='logout'),
    path('register/',register,name='register'),
    path('signup',signup,name='Signup'),
    path('customerslist/',customerslist,name='customerslist'),
    path('customerdetail/<int:pk>/',viewcustomerdetail,name='viewcustomerdetail'),
    path('deletecustomerdetail/<int:pk>/delete/',delcustomerdetail,name='deletecustomerdetail'),
    path('send_email/', send_email,name='sendemail'),
    path('contactus/',contactus,name='contactus'),
    path('contactus/sendemail',send_email,name='sendemail')
]
                                                                                                                                                                                                                                       