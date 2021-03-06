from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from tenders import views
from tendersOffers import views as offersViews
from account.forms import RegistrationForm
from .models import Account
from tendersOffers.models import TenderOffer
from tenders.models import Tender


def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'register/register.html', context)


def login_user(request):
	context = {}

	if request.POST:
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			form = AuthenticationForm()
			context['form'] = form
			context['allTendersOffers'] = offersViews.AllTendersOffers()
			context['CurrentEmailProfile'] = request.user.email
			return render(request, 'account/homePage.html', context)
		else:
			context['form'] = form
			return render(request, 'account/login_user.html', context, status=401)

	else:
		if request.user.is_authenticated:
			context['allTendersOffers'] = offersViews.AllTendersOffers()
			context['CurrentEmailProfile'] = request.user.email
			return render(request, 'account/homePage.html', context)
		else:
			form = AuthenticationForm()
			context['form'] = form
			return render(request, 'account/login_user.html', context)


def homePage(request):
	return render(request, 'account/homePage.html', {})


def logOut(request):
	logout(request)
	return login_user(request)


def Tenders(request):
	return views.Tenders(request)


def MyTenders(request):
	return views.MyTenders(request)


def my_profile(request):
	user = Account.objects.get(username=request.user.username)
	try:
		recent_tender = TenderOffer.objects.filter(email=user.email).last()
		recent_tender = Tender.objects.get(tender_id=recent_tender.tender_id)
	except Exception:
		pass
	recent_tender = 'No Recent Activity'
	return render(request, 'account/myProfile.html', {'user': user, 'recent': recent_tender})
