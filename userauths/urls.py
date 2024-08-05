from django.urls import path
from userauths import views

urlpatterns = [
    path("", views.index,  name=""),

    path("register", views.register, name="register"),

    path("login", views.user_login,  name="login"),

    path("dashboard", views.dashboard,  name="dashboard"),
    
]
