from django.shortcuts import render

from .forms import contactForm

def contact_us(request):
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'account/homePage.html', {'form':form})
		else:
			return render(request,'contact/contact-us.html', {'form': form})
	else:
		form = contactForm()
		return render(request,'contact/contact-us.html', {'form': form})