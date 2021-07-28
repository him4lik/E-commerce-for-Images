from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.
class User(AbstractUser):
	email_or_phone=models.CharField(max_length=50, unique=True, verbose_name='Email or Phone')
	is_buyer=models.BooleanField(choices=[(True, 'Buyer'), (False,'Seller' )], default=True, null=True)
	email=None
	username=None
	first_name=models.CharField(max_length=20)
	last_name=models.CharField(max_length=20)
	contact_email=models.EmailField(max_length=40)

	USERNAME_FIELD='email_or_phone'
	REQUIRED_FIELDS=[]

	
	class custom_manager(BaseUserManager):
		def create_user(self, email_or_phone, password):
			user = self.model(
			email_or_phone=email_or_phone
			)
			user.set_password(password)
			user.save()
			return user
		def create_superuser(self, email_or_phone, password):
			user = self.create_user(
			email_or_phone=email_or_phone,
			password=password,
			)
			user.is_staff = True
			user.is_superuser = True
			user.is_buyer = None
			user.save()
			return user

	objects=custom_manager()


