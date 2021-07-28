from django.shortcuts import render
from custom_auth.models import User
from django import views
from .forms import hire_form
# Create your views here.

class hire_inquiry(views.View):
	template_name='hire/hire.html'
	form=hire_form
	

	def get(self, request, idd):
		fm=self.form
		artist=User.objects.get(image_to_sell__id=idd)
		context={'form':fm,'artist': artist}
		return render(request, self.template_name, context)

	def post(self, request, idd):
		fm=self.form(request.POST)
		artist=User.objects.get(image_to_sell__id=idd)
		context={'form':fm,'artist': artist}
		if fm.is_valid():
			context['flag']=1
		return render(request, self.template_name, context)