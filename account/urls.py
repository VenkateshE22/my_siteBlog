from django.urls import path
from . import views
urlpatterns=[
    path("register/", views.register_request, name="register"),
    path("logIn/", views.login_request, name="logIn"),
    path("logout/", views.logout, name="logout"),
]