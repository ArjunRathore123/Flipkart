from django.urls import path
from .views import sellerlogin,sellerindex,sellerreg,sellerslist,viewsell,deletesell

urlpatterns = [
  
    path('sellerlogin/',sellerlogin,name='sellerlogin'),
    path('sellerindex/',sellerindex,name='sellerindex'),
    path('sellreg/',sellerreg,name='sellerreg'),
    path('sellerslist/',sellerslist,name='sellerslist'),
    path('viewseller/<int:pk>/',viewsell,name="Viewseller"),
    path('deleteseller/<int:pk>/delete/',deletesell,name='Deleteseller'),
    
]