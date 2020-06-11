from django.shortcuts import render
from django.contrib.auth import logout
from . import models
from django.contrib.auth.forms import AuthenticationForm
from tenders import views
from tendersOffers import views as offersViews
from .forms import CommentForm


def homePage(request):
	return render(request, 'account/homePage.html', {})


def logOut(request):
	logout(request)
	form = AuthenticationForm()
	return render(request, 'account/login_user.html', {'form': form})


def Tenders(request):
	ad = request.user.is_admin
	max = 0
	id = 0
	all_tenders = models.Tender.objects.filter(winner='')
	for ten in all_tenders:
		if ten.Count_of_applied > max:
			max = ten.Count_of_applied
			id = ten.tender_id
	return render(request, 'tenders/Tenders.html', {'tenders': all_tenders, 'message': '', 'tenderId': None, 'max_ten': id, 'is_ad': ad})


def TenderPage(request, id=None):
	context = {}

	form = CommentForm()
	context['form'] = form
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = models.Comment.objects.create(comment_name=request.user.get_username(), comment_content=form.cleaned_data['comment_content'], tender_id=id)
			comment.save()
			tender = models.Tender.objects.get(tender_id=id)
			context['tender'] = tender
			comments = models.Comment.objects.filter(tender_id=id)
			context['comments'] = comments

		else:
			return render(request, 'tenders/tenderInfo.html', context)

	else:
		tender = models.Tender.objects.get(tender_id=id)
		context['tender'] = tender
		try:
			comments = models.Comment.objects.filter(tender_id=id)
			context['comments'] = comments
		except Exception:
			context['comments'] = []
		return render(request, 'tenders/tenderInfo.html', context)
	return render(request, 'tenders/tenderInfo.html', context)


def CloseTenders(request):
	all_tenders = models.Tender.objects.all()
	return render(request, 'tenders/CloseTenders.html', {'tenders': all_tenders, 'message': '', 'tenderId': None})


def RegisterOffer(request):
	all_tenders = models.Tender.objects.all()
	if 'tenId' in request.POST:
		if request.POST.get("Offer") == '':
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
	ad = request.user.is_admin
	max = 0
	id = 0
	for ten in all_tenders:
		if ten.Count_of_applied > max:
			max = ten.Count_of_applied
			id = ten.tender_id
	all_tendersDic['max_ten'] = id
	all_tendersDic['is_ad'] = ad
	return render(request, 'tenders/Tenders.html', all_tendersDic)


def Search(request):
	ad = request.user.is_admin
	max = 0
	id = 0
	all_tenders = models.Tender.objects.filter(tender_id=request.POST.get("search"))
	for ten in all_tenders:
		if ten.Count_of_applied > max:
			max = ten.Count_of_applied
			id = ten.tender_id
	return render(request, 'tenders/Tenders.html', {'tenders': all_tenders, 'message': '', 'tenderId': None, 'max_ten': id, 'is_ad': ad})


def DeleteOffer(request):
	views.DeleteOffer(request)


def MyTenders(request):
	context = {}
	form = AuthenticationForm()
	context['form'] = form
	context['allTendersOffers'] = offersViews.AllTendersOffers()
	context['CurrentEmailProfile'] = request.user.email
	return render(request, 'tenders/Mytenders.html', context)
