from django.shortcuts import render, HttpResponse, redirect
from .models import Image
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from custom_auth.models import User
from django import views
from .forms import guest_checkout_form, post_to_sell_form
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from main_site.decorators import allowed_users, allowed_users_idd
from buy_images.settings import client, KEY_ID
from payment.models import order
from datetime import datetime
from buy_images.settings import client
# Create your views here.
def images(request):
	template_name='images/images.html'
	image_queryset=Image.objects.all()
	data=(image_queryset)
	context={'data': data}
	return render(request, template_name, context)

@allowed_users_idd(allowed_roles=['buyer', 'guest'])
def add(request, idd):
	image=Image.objects.get(pk=idd)
	image.cart_user.add(request.user)
	return redirect('/images/')


@allowed_users_idd(allowed_roles=['buyer', 'guest'])
def buy_now(request, idd):
	template_name='images/buy_now.html'
	image=Image.objects.get(pk=idd)
	now = datetime.now()
	order_time= now.strftime("%m/%d/%Y, %H:%M:%S")
	order_obj=order.objects.create(image=image, user=request.user, order_id=str(request.user.id)+order_time+str(image.id), amount=image.amount)
	amount = (image.amount)*100
	GST=0.1*amount
	total=amount+(GST)
	currency = 'INR'
	receipt = 'order_rcptid_11'
	notes = {'Shipping address': 'Bommanahalli, Bangalore'}  
	order_id=client.order.create(dict(amount=total, currency=currency, receipt=receipt, notes=notes))
	print(order_id['id'])
	order_obj.rp_order_id=str(order_id['id'])
	order_obj.save()
	context={'image': image, 'KEY_ID': KEY_ID, 'amount': amount, 'currency': currency, 'receipt_id': receipt, 'order_id': order_id['id'] , 'price':{'GST': GST/100, 'total': total/100}}
	return render(request, template_name, context)

@allowed_users(allowed_roles=['buyer', 'guest'])
def buy_all(request):
	template_name='images/buy_all.html'
	images=request.user.image_set.all()
	context={'images': images}
	return render(request, template_name, context)



class guest_checkout(views.View):
	template_name='images/guest_checkout.html'
	form=guest_checkout_form
	def get(self, request):
		fm=self.form()
		context={'form': fm}
		return render(request,  self.template_name, context)

	def post(self,request):
		fm=self.form(request.POST)
		context={'form': fm}
		if fm.is_valid():
			return redirect('payment_options')
		return render(request, self.template_name, context)

class post_to_sell(LoginRequiredMixin, views.View):
	
	login_url = 'login_user'
	template_name='images/post_to_sell.html'
	form=post_to_sell_form
	def get(self, request):
		user=User.objects.get(id=request.user.id)
		fm=self.form(initial={'artist': request.user})
		context={'form': fm}
		return render(request,  self.template_name, context)

	def post(self,request):
		fm=self.form(request.POST, request.FILES)
		context={'form': fm}
		if fm.is_valid():
			fm.save()
			return redirect('payment_options')
		return render(request, self.template_name, context)



def artist_images(request, idd):
	template_name='images/images.html'
	user=User.objects.get(pk=idd)
	image_queryset=user.image_to_sell.all()
	data=(image_queryset)
	context={'data': data, 'artist_name': user.first_name}
	return render(request, template_name, context)


@csrf_exempt
def download_bought(request):
	download_template='images/download_template.html'
	failed_template='images/failed_template.html'
	p_dict={
	'razorpay_order_id':request.POST['razorpay_order_id'],
	'razorpay_payment_id':request.POST['razorpay_payment_id'],
	'razorpay_signature':request.POST['razorpay_signature'],
	}
	print(p_dict)
	order_obj=order.objects.get(rp_order_id=p_dict['razorpay_order_id'])
	order_obj.rp_payment_id=p_dict['razorpay_payment_id']
	order_obj.rp_signature=p_dict['razorpay_signature']
	order_obj.save()
	result=client.utility.verify_payment_signature(p_dict)
	if result==None:
		amount=order_obj.amount
		order_obj.status=1
		order_obj.save()
		return render(request, download_template)
	else:
		return render(request, failed_template)
