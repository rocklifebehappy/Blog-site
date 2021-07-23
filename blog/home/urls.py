from django.urls import path
from .views import about, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("profile", UserPostListView.as_view(), name="profile"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/update/<int:pk>/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/delete/<int:pk>/", PostDeleteView.as_view(), name="post-delete"),
    path("about/", about, name="about"),
]
