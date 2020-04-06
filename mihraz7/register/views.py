from django.shortcuts import render
from account.forms import RegistrationForm


def registerPage(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()


    context ={'form':form}
    return render(request, 'register/register.html',context)