from django.urls import path, include
from . import views as images_views
from hire import views as hire_views
from main_site.decorators import allowed_users



urlpatterns=[
	path('', images_views.images, name='images'),
	path('artist_images/<int:idd>', images_views.artist_images, name='artist_images'),
	path('add/<int:idd>/', images_views.add, name='image_add'),
	path('buy_now/<int:idd>/', images_views.buy_now, name='image_buy_now'),
	path('buy_all/', images_views.buy_all, name='image_buy_all'),
	path('download_bought/', images_views.download_bought, name='download_bought'),
	path('guest_checkout/', allowed_users(allowed_roles=['guest'])(images_views.guest_checkout.as_view()), name='guest_checkout'), 
	path('image_hire/<int:idd>/', include('hire.urls')),
	path('post_to_sell/', allowed_users(allowed_roles=['seller', 'guest'])(images_views.post_to_sell.as_view()), name='post_to_sell'),
]

