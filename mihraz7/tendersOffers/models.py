from django.db import models

class TenderOffer(models.Model):
    id                      = models.AutoField(primary_key=True)    
    tender_id               = models.CharField(max_length=50)
    first_name				= models.CharField(max_length=30)
    last_name 				= models.CharField(max_length=30)
    email 					= models.EmailField(verbose_name="email", max_length=60)
    offer                   = models.CharField(max_length=100)

    def __str__(self):
        return self.tender_id