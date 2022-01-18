"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# will access userapp views directly instead of creating a url file in userapp and including it here
# from usersapp import views as v
# routes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('usersapp.urls', 'usersapp'), namespace='usersapp')),
    path('', include('App1.urls')),
    # has /login path and has a view that renders registration/login.html for the html (need to create registration/login.html locally)
    # path('', include("django.contrib.auth.urls")),

]
