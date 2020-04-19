from django.urls import path, include
from . import views

from account.views import (
    registration_view
)

urlpatterns = [
    path('', views.login_user),
    path('login_user/',views.login_user)
]
