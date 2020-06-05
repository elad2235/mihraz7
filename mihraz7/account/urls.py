from django.urls import path
from . import views
from suppliers import views as supp_views
from contact import views as contact_views


urlpatterns = [
    path('login_user/', views.login_user, name='login'),
    path('homePage/', views.homePage, name='homePage'),
    path('logOut/', views.logOut, name="account_logout"),
    path('', views.login_user, name='home'),
    path('Tenders/', views.Tenders, name="Tender"),
    path('suppliers/', supp_views.supp_page, name="supp_page"),
    path('contact/', contact_views.contact_us, name="contact_us"),
    path('MyTenders/', views.MyTenders, name="my_tenders"),
]
