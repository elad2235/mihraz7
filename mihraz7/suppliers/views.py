from django.shortcuts import render

from . import models
from suppliers import views

def supp_page(request):
	all_suppliers = models.Supplier.objects.all()
	return render(request,'suppliers/supp_page.html',{'suppliers': all_suppliers})