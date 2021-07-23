from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm(UserCreationForm):
	"""
	Form for the user registration.
	:model : 'auth.user'
	"""
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	"""
	Form for the user edit.
	:model : 'auth.user'
	"""
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
	"""
	Form for the profile update of the user.
	:model : 'auth.user.profile'
	"""
	class Meta:
		model = Profile
		fields = ["image", "fullname", "address", "status"]
