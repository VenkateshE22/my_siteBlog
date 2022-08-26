from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path(
        "posts/<slug:slug>",
        views.post_detail,
        name="post-detail-page",
    ),
    path("upload/", views.upload, name="upload"),
    path("my-posts/", views.dashboard, name="my-posts"),
    path("add_category/", views.category_view, name="add_category"),
    path("update_blog/<slug>", views.update_blog, name="update_blog"),
    path("delete-blog/<slug>", views.delete_blog, name="delete_blog"),
]
