from django.shortcuts import render
from . import models
from tenders import models as tenderModel

def RegisterOffer(request):
    tenderId = request.POST.get("tenId")
    tenderName = tenderModel.Tender.objects.get(tender_id=request.POST.get("tenId")).tender_name
    firstName = request.user.first_name
    lastName = request.user.last_name
    Email = request.user.email
    Offer = request.POST.get("Offer")
    count = tenderModel.Tender.objects.get(tender_id=request.POST.get("tenId")).Count_of_applied
    tenderModel.Tender.objects.filter(tender_id=tenderId).update(Count_of_applied=count+1)
    newOffer = models.TenderOffer(tender_id=tenderId,tender_name=tenderName,first_name=firstName,last_name=lastName,email=Email,offer=Offer)
    newOffer.save()

def DeleteOffer(request):
    if(models.TenderOffer.objects.filter(tender_id=request.POST.get("tenIdDelete"),email=request.user.email).count()>0):
        count = tenderModel.Tender.objects.get(tender_id=request.POST.get("tenIdDelete")).Count_of_applied
        tenderModel.Tender.objects.filter(tender_id=request.POST.get("tenIdDelete")).update(Count_of_applied=count-models.TenderOffer.objects.filter(tender_id=request.POST.get("tenIdDelete"),email=request.user.email).count())
        models.TenderOffer.objects.filter(tender_id=request.POST.get("tenIdDelete"),email=request.user.email).delete()

def AllTendersOffers():
    return models.TenderOffer.objects.all()