from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
# routes
urlpatterns = [
    path('register/', views.register, name='register'),
    # path('createuser/', views.createuser, name="createuser"),
    path("login/", views.loginpage, name="login"),
    # path("loginuser/", views.loginuser, name="loginuser"),
    path("logout/", views.logoutuser, name="logoutuser"),
    path("change-password/", auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
]
