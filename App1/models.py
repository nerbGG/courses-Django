import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


# has the names of the courses and the names of the instructors
class AllCourses(models.Model):
    user = models.ManyToManyField(User)
    courseName = models.CharField(max_length=200)
    instrucName = models.CharField(max_length=100)
    startedFrom = models.DateTimeField('Started from')

    def __str__(self):
        return self.courseName

    def was_published_recently(self):
        return self.startedFrom >= timezone.now() - datetime.timedelta(days=1)


class Details(models.Model):
    # each detail is related to a single course
    course = models.ForeignKey(AllCourses, on_delete=models.CASCADE)
    # sp = models.CharField(max_length=500)
    # il = models.CharField(max_length=500)
    ct = models.CharField(max_length=500)
    your_choice = models.BooleanField(default=False)

    def __str__(self):
        return str(self.ct)
