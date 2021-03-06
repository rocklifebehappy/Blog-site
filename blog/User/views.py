from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


# Create your views here.

def register(request):
	"""
	Redirects to the register page.

	:param request: HTTP request sent by the user.
	:return: render (returns HTTP response to the HTTP request)
	"""
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get("username")
			messages.success(request, f'Account created for {username}!')
			return redirect("login")
	else:
		form = UserRegistrationForm()
	context = {
		'form': form
	}
	return render(request, 'users/register.html', context)


@login_required
def edit_profile(request):
	"""
	Redirects to the profile edit page.

	:param request: HTTP request sent by the user.
	:return: render (returns HTTP response to the HTTP request)
	"""
	u_form = UserUpdateForm(request.POST, instance=request.user)
	p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
	if request.method == 'POST':
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			username = u_form.cleaned_data.get("username")
			messages.success(request, f'Profile edited for {username}!')
			return redirect("profile")
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'users/edit_profile.html', context)
