from django.urls import path, include
from . import views
from contact import views

urlpatterns = [
    path('', views.contact_us, name="contact_us")
]