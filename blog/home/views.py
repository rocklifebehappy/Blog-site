from django.shortcuts import render


# We are mostly using the function based views.

def home(request):
	"""

	:param request:
	:return:
	"""
	context = {

	}
	return render(request, "home.html", context=context)


def about(request):
	"""

	:param request:
	:return:
	"""
	return render(request, "about.html", context={})
