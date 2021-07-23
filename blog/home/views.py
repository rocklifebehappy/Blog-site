from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from .models import World


# We are mostly using the function based views.
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class PostListView(ListView):
	"""
	This class is used in he homepage. It sends the posts from the model to the home page.
	"""
	model = World
	template_name = 'home.html'
	context_object_name = 'posts'
	ordering = '-date_published'
	paginate_by = 2


class UserPostListView(LoginRequiredMixin, ListView):
	"""
	This is for the profile page. It sends post related only to the user
	"""
	model = World
	template_name = "users/profile.html"
	context_object_name = "posts"
	ordering = "-date_published"
	paginate_by = 2

	def get_queryset(self):
		"""
		This is the query that is executed to obtain the data.

		:return: posts related only to the user.
		"""
		return World.objects.filter(author=self.request.user).order_by(self.ordering)


class PostDetailView(DetailView):
	"""
	This directs to the detail of the post.
	"""
	model = World
	template_name = "post_detail.html"


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	"""
	To delete the post.
	It inherits LoginRequiredMixin, UserPassesTestMixin to ensure the login and proper authentication.
	"""
	model = World
	template_name = "post_confirm_delete.html"
	success_url = "/"

	def test_func(self):
		"""
		This is the test to ensure if the user has the proper authentication to delete the post.
		Author of the post and the user must be same to delete the post.
		:return: True if author and user are same else False(that gives 403 error).
		"""
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False


class PostCreateView(LoginRequiredMixin, CreateView):
	"""
	It gives the post create.
	It inherits the LoginRequiredMixin to ensure the login is done.
	"""
	model = World
	template_name = "post_form.html"
	fields = ["title", "image", "contents"]

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	"""
	To update the current post.
	It inherits LoginRequiredMixin, UserPassesTestMixin to ensure the login and proper authentication.
	"""
	model = World
	template_name = "post_form.html"
	fields = ["title", "image", "contents"]

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		"""
		This is the test to ensure if the user has the proper authentication to update the post.
		Author of the post and the user must be same to update the post.
		:return: True if author and user are same else False(that gives 403 error).
		"""
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False


def about(request):
	"""

	:param request:
	:return:
	"""
	return render(request, "about.html", context={})
