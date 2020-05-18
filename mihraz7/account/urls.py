from django.urls import path, include
from . import views

from account.views import (
    registration_view
)

urlpatterns = [
    path('login_user/',views.login_user,name='login'),
    path('homePage/',views.homePage,name='homePage'),
    path('logOut/',views.logOut,name="account_logout"),
    path('', views.login_user, name='home'),
    path('Tenders/',views.Tenders,name="Tender"),
]
