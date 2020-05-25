from django.urls import path, include
from . import views
from suppliers import views as supp_views

from account.views import (
    registration_view
)

urlpatterns = [
    path('homePage/',views.homePage,name='homePage'),
    path('logOut/',views.logOut,name="account_logout"),
    path('Tenders/',views.Tenders,name="Tender"),
    path('CloseTenders/',views.CloseTenders,name="CloseTenders"),
    path('RegisterOffer/',views.RegisterOffer),
    path('suppliers/', supp_views.supp_page, name="supp_page"),
]
