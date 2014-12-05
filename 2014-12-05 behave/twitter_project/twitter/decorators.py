from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def no_login_please(f):
	def wrapper(request, *args, **kargs):
		user = request.user
		if user.is_authenticated():
			return HttpResponseRedirect(reverse("twitter:home"))
		else:
			return f(request, *args, **kargs)
	return wrapper


