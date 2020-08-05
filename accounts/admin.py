from django.contrib import admin
from .models import Courses, UserProfile, Attends
# Register your models here.

admin.site.register(Courses)
admin.site.register(UserProfile)
admin.site.register(Attends)
