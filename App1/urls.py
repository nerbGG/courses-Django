from django.urls import path
from . import views

app_name = 'App1'
#routes
urlpatterns = [
    path('', views.Courses, name='home-page'),
    path('<int:course_id>/', views.detail, name='detail'),
    path('<int:course_id>/yourchoice/', views.yourchoice, name='yourchoice'),
]
