from django.urls import path
from . import views

# routes
urlpatterns = [
    path('register/', views.register, name='register'),
    # path('createuser/', views.createuser, name="createuser"),
    path("login/", views.loginpage, name="login"),
    # path("loginuser/", views.loginuser, name="loginuser"),
    path("logout/", views.logoutuser, name="logoutuser"),
]
