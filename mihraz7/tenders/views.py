from django.shortcuts import render
from django.contrib.auth import login,logout

from . import models
from tendersOffers import views

def homePage(request):
	context = {}
	context['tenders'] = models.Tender.objects.all()
	context['allTendersOffers'] = views.AllTendersOffers()
	context['CurrentEmailProfile'] = request.user.email
	return render(request,'account/homePage.html',context)

def logOut(request):
	logout(request)
	return render(request,'account/login_user.html',{})

def Tenders(request):
	all_tenders = models.Tender.objects.all()
	return render(request,'tenders/Tenders.html',{ 'tenders': all_tenders, 'message':'','tenderId':None})

def RegisterOffer(request):
	all_tenders = models.Tender.objects.all()
	if 'tenId' in request.POST:
		all_tendersDic = {
			'tenderId':request.POST.get("tenId"),
			'message':'Offer Accepted!',
			'tenders': all_tenders
		}
		views.RegisterOffer(request)
	else:
		all_tendersDic = {
			'tenderId':request.POST.get("tenIdDelete"),
			'message':'Offer Deleted!',
			'tenders': all_tenders
		}
		views.DeleteOffer(request)
	return render(request,'tenders/Tenders.html',all_tendersDic)

def DeleteOffer(request):
	views.DeleteOffer(request)