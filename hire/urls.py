from django.urls import path, include
from . import views as hire_views
from main_site.decorators import allowed_users

urlpatterns=[
	path('', (hire_views.hire_inquiry.as_view()), name='image_hire'),

]