from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	fullname = models.CharField(max_length=40, blank=True, null=True)
	address = models.CharField(max_length=40, blank=True, null=True)
	status = models.TextField(max_length=80, blank=True, null=True)
	image = models.ImageField(default="default.png", upload_to="profile_pics")

	def __str__(self):
		return self.user.username

	def save(self):
		super().save()

		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)
