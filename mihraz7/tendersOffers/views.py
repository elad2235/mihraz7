from django.shortcuts import render
from . import models

def RegisterOffer(request):
    tenderId = request.POST.get("tenId")
    print(tenderId)
    firstName = request.user.first_name
    lastName = request.user.last_name
    Email = request.user.email
    Offer = request.POST.get("Offer")
    print(Offer)
    
    newOffer = models.TenderOffer(tender_id=tenderId,first_name=firstName,last_name=lastName,email=Email,offer=Offer)
    newOffer.save()

def DeleteOffer(request):
    models.TenderOffer.objects.filter(tender_id=request.POST.get("tenIdDelete"),email=request.user.email).delete()

def AllTendersOffers():
    return models.TenderOffer.objects.all()