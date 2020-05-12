from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout

from tenders import views

from account.forms import RegistrationForm


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
			
	else: #GET request
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'register/register.html', context)

def login_user(request):
	context ={}

	if request.POST:
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request,user)
			form = AuthenticationForm()
			context['form']=form
			return render(request,'account/homePage.html',context)
		else:
			context['form']=form
			return render(request,'account/login_user.html',context, status = 401)

	else:
		if request.user.is_authenticated:
			return render(request,'account/homePage.html',context)
		else:
			form = AuthenticationForm()
			context['form']=form
			return render(request,'account/login_user.html',context)

def homePage(request):
	return render(request,'account/homePage.html',{})

def logOut(request):
	logout(request)
	return render(request,'account/login_user.html',{})

def Tenders(request):
	return views.Tenders(request)