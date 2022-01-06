from django.urls import path
from . import views
app_name = 'App1'
#routes
urlpatterns = [
    path('<int:course_id>/', views.detail, name='detail'),
    path('', views.Courses, name='home-page'),
    path('<int:course_id>/yourchoice/', views.yourchoice, name='yourchoice'),
]
