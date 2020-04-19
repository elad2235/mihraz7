from django.contrib import admin
from django.urls import path, include

from account.views import (
    registration_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',include('register.urls')),
    path('login/',include('account.urls')),
    path('account/',include('account.urls'))
]




