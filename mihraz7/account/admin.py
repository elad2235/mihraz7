from django.contrib import admin
from .models import Account
from django.contrib.auth.hashers import make_password

class PasswordUserAdmin(admin.ModelAdmin):
    def save_model(self,request,obj,form,change):
        obj.password = make_password(obj.password)
        obj.user = request.user
        obj.save()

admin.site.register(Account,PasswordUserAdmin)
