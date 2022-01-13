from django.urls import path
from . import views

# routes
urlpatterns = [
    path('register/', views.register, name='register'),
    path('createuser/', views.createuser, name='createuser'),
]
