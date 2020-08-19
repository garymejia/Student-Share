from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class Course(models.Model):
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    professor = models.CharField(max_length=50)
    section = models.PositiveSmallIntegerField()
    crn = models.PositiveSmallIntegerField()
    documents = models.ManyToManyField(Document)
    
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=None)
    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return "%s's profile" % self.user

