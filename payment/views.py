from django.shortcuts import render
from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
import razorpay
from buy_images import settings
# Create your views here.
class payment_options(LoginRequiredMixin, views.View):
	login_url = 'login_user'
	template_name='payment/payment_options.html'

	def get(self, request):
		return render(request, self.template_name)
	def post(self, request):
		return render(request, self.template_name)