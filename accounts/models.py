from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Courses(models.Model):
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    professor = models.CharField(max_length=50)
    section = models.PositiveSmallIntegerField()
    crn = models.PositiveSmallIntegerField()
    userprofiles = models.ManyToManyField('UserProfile', through='Attends')

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.ManyToManyField('Courses', through='Attends')

    def __str__(self):
        return "%s's profile" % self.user

#Juction table
class Attends(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    

