from django.shortcuts import render

# We are mostly using the function based views.

posts = [
	{
		'author': 'Roshan Shrestha',
		'title': 'Blog post 1',
		'content': 'First Post Content',
		'date_posted': 'August 1, 2018'
	}
]


def home(request):
	"""

	:param request:
	:return:
	"""
	context = {
		'posts': posts
	}
	return render(request, "home.html", context=context)


def about(request):
	"""

	:param request:
	:return:
	"""
	return render(request, "about.html", context={})
