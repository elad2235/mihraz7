from django.contrib import admin
from django.urls import path, include 
from . import views

from account.views import (
    registration_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',include('register.urls')),
    path('/', RedirectView.as_view(pattern_name='account:home'),
]
