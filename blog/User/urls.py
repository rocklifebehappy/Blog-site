from django.urls import path
from .views import register, edit_profile

urlpatterns = [
    path("", register, name="register"),
    path("edit_profile", edit_profile, name="edit_profile")
]
