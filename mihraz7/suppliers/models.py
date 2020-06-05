from django.db import models


class Supplier(models.Model):
    Supplier_name = models.CharField(max_length=50)
    Supplier_id = models.CharField(max_length=50)
    Service = models.CharField(max_length=50)

    def __str__(self):
        return self.Supplier_name
