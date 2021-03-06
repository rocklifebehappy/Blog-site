from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class World(models.Model):
	"""
	Model for the world category.

	Attributes:
		title (str): The title of the post.
		author (User): The author of the post.
		contents (str): The contents or the paragraph of the post.
		image (image): The image of the post.
		date_published (date): The date published.
	"""
	title = models.CharField(max_length=80, blank=False, null=False)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	contents = models.TextField(max_length=1000)
	image = models.ImageField(upload_to="images", blank=True, null=True)
	date_published = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""
		For returning the object identification. It may be any attribute of the required object.

		:return: returns the title attribute of the object.
		"""
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})


class InformationTechnology(models.Model):
	"""
	Model for the information category category.

	Attributes:
		title (str): The title of the post.
		author (User): The author of the post.
		contents (str): The contents or the paragraph of the post.
		image (image): The image of the post.
		date_published (date): The date published.
	"""
	title = models.CharField(max_length=80, blank=False, null=False)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	contents = models.TextField(max_length=1000)
	image = models.ImageField(upload_to="images", blank=True, null=True)
	date_published = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""
		For returning the object identification. It may be any attribute of the required object.

		:return: returns the title attribute of the object.
		"""
		return self.title


class RemoteDevelopment(models.Model):
	"""
	Model for the Remote Development category.

	Attributes:
		title (str): The title of the post.
		author (User): The author of the post.
		contents (str): The contents or the paragraph of the post.
		image (image): The image of the post.
		date_published (date): The date published.
	"""
	title = models.CharField(max_length=80, blank=False, null=False)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	contents = models.TextField(max_length=1000)
	image = models.ImageField(upload_to="images", blank=True, null=True)
	date_published = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""
		For returning the object identification. It may be any attribute of the required object.

		:return: returns the title attribute of the object.
		"""
		return self.title


class Agriculture(models.Model):
	"""
	Model for the agriculture category.

	Attributes:
		title (str): The title of the post.
		author (User): The author of the post.
		contents (str): The contents or the paragraph of the post.
		image (image): The image of the post.
		date_published (date): The date published.
	"""
	title = models.CharField(max_length=80, blank=False, null=False)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	contents = models.TextField(max_length=1000)
	image = models.ImageField(upload_to="images", blank=True, null=True)
	date_published = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""
		For returning the object identification. It may be any attribute of the required object.

		:return: returns the title attribute of the object.
		"""
		return self.title


class Bioinformatics(models.Model):
	"""
	Model for the Bioinformatics category.

	Attributes:
		title (str): The title of the post.
		author (User): The author of the post.
		contents (str): The contents or the paragraph of the post.
		image (image): The image of the post.
		date_published (date): The date published.
	"""
	title = models.CharField(max_length=80, blank=False, null=False)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	contents = models.TextField(max_length=1000)
	image = models.ImageField(upload_to="images", blank=True, null=True)
	date_published = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""
		For returning the object identification. It may be any attribute of the required object.

		:return: returns the title attribute of the object.
		"""
		return self.title


class EnvironmentalTechnology(models.Model):
	"""
	Model for the Environmental category.

	Attributes:
		title (str): The title of the post.
		author (User): The author of the post.
		contents (str): The contents or the paragraph of the post.
		image (image): The image of the post.
		date_published (date): The date published.
	"""
	title = models.CharField(max_length=80, blank=False, null=False)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	contents = models.TextField(max_length=1000)
	image = models.ImageField(upload_to="images", blank=True, null=True)
	date_published = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""
		For returning the object identification. It may be any attribute of the required object.

		:return: returns the title attribute of the object.
		"""
		return self.title
