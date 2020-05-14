from django.db import models

class Tender(models.Model):
    tender_name = models.CharField(max_length=50)
    tender_id = models.CharField(max_length=50,unique=True)
    winner = models.CharField(max_length=50, blank=True)
    files = models.CharField(max_length=100, blank=True)
    online_payment = models.CharField(max_length=100,blank=True)
    url = models.CharField(max_length=100, blank=True)
    end_date = models.DateField(auto_now=False,auto_now_add=False,blank=True)
    update_date = models.DateField(auto_now=False,auto_now_add=False,blank=True)


    def __str__(self):
        return self.tender_name

