from django.shortcuts import redirect


def allowed_users(allowed_roles=[]):
	def user_permission(func):
		def wrapper(request, ):
			
			if not request.user.is_authenticated:
				if 'guest' in allowed_roles:
					return func(request)
				else:
					return redirect('home')

			group=request.user.groups.all()[0].name
			if group in allowed_roles:
				return func(request)
			else:
				return redirect('home')
		return wrapper
	return user_permission

def allowed_users_idd(allowed_roles=[]):
	def user_permission(func):
		def wrapper(request, idd):
			
			if not request.user.is_authenticated:
				if 'guest' in allowed_roles:
					return func(request)
				else:
					return redirect('home')

			group=request.user.groups.all()[0].name
			if group in allowed_roles:
				return func(request, idd)
			else:
				return redirect('home', idd)
		return wrapper
	return user_permission
