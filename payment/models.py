from django.db import models

# Create your models here.
class Payment(models.Model):
    cash="ch"
    card="cd"
    online="on"
    pay={
        card:"Card",
        cash:"Cash",
        online:"Online",
    }
    stat={
        "pending":"Pending",
        "done":"Done",
        "cancelling":"Cancelling",
    }
    
    payment_method=models.CharField(max_length=10,choices=pay)
    payment =models.IntegerField()
    status = models.CharField(max_length=10,choices=stat)
    created_on = models.DateTimeField(auto_now_add=True)







