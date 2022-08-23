from django.urls import path
from . import views
urlpatterns=[
    path("register/", views.register_request, name="register"),
    path("LogIn/", views.login_request, name="LogIn"),
]