from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, first_name, last_name, phone, password=None,is_admin=False):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')
		if not first_name:
			raise ValueError('Users must have first name')
		if not last_name:
			raise ValueError('Users must have last name')
		if not phone:
			raise ValueError('Users must have phone')
	
		user = self.model(
			email=self.normalize_email(email),
			username=username,
			first_name=first_name,
			last_name=last_name,
			phone=phone,
			is_admin=is_admin
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, first_name, last_name, phone, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
			first_name=first_name,
			last_name=last_name,
			phone=phone
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)
	first_name				= models.CharField(max_length=30)
	last_name 				= models.CharField(max_length=30)
	phone 					= models.CharField(max_length=30)



	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email','first_name','last_name','phone']

	objects = MyAccountManager()

	def __str__(self):
		return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True





