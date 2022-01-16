# Generated by Django 4.0.1 on 2022-01-16 17:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App1', '0003_alter_allcourses_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allcourses',
            name='user',
        ),
        migrations.AddField(
            model_name='allcourses',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
