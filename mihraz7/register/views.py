from django.shortcuts import render
from account.forms import RegistrationForm
from django.http import HttpResponse


def registerPage(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Thanks for contacting us!')

        else:
            context = {'form': form}
            return render(request, 'register/register.html', context)

    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'register/register.html', context)
