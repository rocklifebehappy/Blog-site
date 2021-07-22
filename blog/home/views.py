from abc import ABC

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from .models import World


# We are mostly using the function based views.
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class PostListView(ListView):
	model = World
	template_name = 'home.html'
	context_object_name = 'posts'
	ordering = '-date_published'


class PostDetailView(DetailView):
	model = World
	template_name = "post_detail.html"


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = World
	template_name = "post_confirm_delete.html"
	success_url = "/"

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False


class PostCreateView(LoginRequiredMixin, CreateView):
	model = World
	template_name = "post_form.html"
	fields = ["title", "image", "contents"]

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = World
	template_name = "post_form.html"
	fields = ["title", "image", "contents"]

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
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
