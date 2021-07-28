from django.urls import path, include
from . import views as auth_views
from main_site.decorators import allowed_users

urlpatterns=[
	path('login_user/', 
			include([ 
			path('', allowed_users(allowed_roles=['guest'])(auth_views.login_user.as_view()), name='login_user'),
			path('forgot_password/', auth_views.forgot_password, name='forgot_password'),
			])
		),
	path('register/', allowed_users(allowed_roles=['guest'])(auth_views.register.as_view()), name='register'),
	path('logout_user/', auth_views.logout_user , name='logout_user'),
	path('dashboard/', allowed_users(allowed_roles=['buyer', 'seller'])(auth_views.dashboard.as_view()), name='dashboard'),
	path('delete/', allowed_users(allowed_roles=['buyer', 'seller'])(auth_views.delete_account.as_view()), name='delete_account')
]