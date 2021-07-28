from django.urls import path
from . import views as payment_views



urlpatterns=[
	path('', payment_views.payment_options.as_view(), name='payment_options')

]