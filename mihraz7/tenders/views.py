from django.shortcuts import render

from . import models


def homePage(request):
	return render(request,'account/homePage.html',{})

def logOut(request):
	logout(request)
	return render(request,'account/login_user.html',{})

def Tenders(request):
	all_tenders = models.Tender.objects.all()
	return render(request,'tenders/Tenders.html',{ 'tenders': all_tenders })

