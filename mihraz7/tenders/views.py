from django.shortcuts import render
from django.contrib.auth import login,logout

from . import models
from tendersOffers import views
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from tenders import views
from tendersOffers import views as offersViews
from account.forms import RegistrationForm

def homePage(request):
	return render(request,'account/homePage.html',{})

def logOut(request):
	logout(request)
	return render(request,'account/login_user.html',{})

def Tenders(request):
	all_tenders = models.Tender.objects.all()
	
	return render(request,'tenders/Tenders.html',{ 'tenders': all_tenders, 'message':'','tenderId':None})

def CloseTenders(request):
	all_tenders = models.Tender.objects.all()
	return render(request,'tenders/CloseTenders.html',{ 'tenders': all_tenders, 'message':'','tenderId':None})

def RegisterOffer(request):
    all_tenders = models.Tender.objects.all()
    if 'tenId' in request.POST:
        if request.POST.get("Offer") is '':
            all_tendersDic = {
                'tenderId': request.POST.get("tenId"),
                'message': 'Empty Offer!',
                'tenders': all_tenders
            }
        else:
            all_tendersDic = {
                'tenderId': request.POST.get("tenId"),
                'message': 'Offer Accepted!',
                'tenders': all_tenders
            }
            offersViews.RegisterOffer(request)
    else:
        all_tendersDic = {
            'tenderId': request.POST.get("tenIdDelete"),
            'message': 'Offer Deleted!',
            'tenders': all_tenders
        }
        offersViews.DeleteOffer(request)
    return render(request, 'tenders/Tenders.html', all_tendersDic)

def Search(request):
    all_tendersDic = {
        'tenderId': '',
        'message': '',
        'tenders': models.Tender.objects.filter(tender_id=request.POST.get("search"))
    }
    return render(request, 'tenders/Tenders.html', all_tendersDic)

def DeleteOffer(request):
	views.DeleteOffer(request)

def MyTenders(request):
	context={}
	form = AuthenticationForm()
	context['form'] = form
	context['allTendersOffers'] = offersViews.AllTendersOffers()
	context['CurrentEmailProfile'] = request.user.email
	return render(request,'tenders/Mytenders.html',context)

	