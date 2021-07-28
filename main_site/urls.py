
from django.urls import path, include
from main_site import views as home_views



urlpatterns=[
	path('', home_views.home, name='home'),
	path('auth/', include('custom_auth.urls')),
	path('images/', include('images.urls')),
	path('contact_us/', home_views.contact, name='contact'),
	path('cart/', home_views.cart, name='cart'),
	path('payment/', include('payment.urls')),
	path('remove/<idd>', home_views.remove, name='remove_from_cart')
]