from django.shortcuts import render, redirect
from django import views
from custom_auth.forms import login_form, register_form
from django.contrib.auth import login, logout, authenticate
from .decorators import allowed_users
from images.models import Image
from custom_auth.models import User


def home(request):
	return render(request, 'main_site/home.html')



def contact(request):
	return render(request, 'main_site/contact.html')

@allowed_users(allowed_roles=['buyer', 'guest'])
def cart(request):
	cart=request.user.image_set.all()
	context={'cart': cart}
	return render(request, 'main_site/cart.html', context)

def remove(request, idd):
	image=Image.objects.get(pk=idd)
	request.user.image_set.remove(image)
	return redirect('cart')