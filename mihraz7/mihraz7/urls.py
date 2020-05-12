from django.contrib import admin
from django.urls import path, include
from account import views as account_views

from account.views import (
    registration_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',include('register.urls')),
    path('login/',include('account.urls')),
    path('account/',include('account.urls')),
    path('tenders/',include('tenders.urls')),
    path('',account_views.login_user)
]




