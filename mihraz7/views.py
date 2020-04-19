from django.shortcuts import render, redirect

def homePage(request):
    return redirect('account/login_user')