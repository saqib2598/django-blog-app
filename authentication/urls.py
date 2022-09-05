from . import views
from django.urls import path

urlpatterns = [
    path("register", views.register_req, name='register'),
    path("login", views.login_req, name="login"),
    path("logout", views.logout_req, name= "logout"),
]