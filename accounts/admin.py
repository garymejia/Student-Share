from django.contrib import admin
from .models import Course, UserProfile#, Attends
# Register your models here.

admin.site.register(Course)
admin.site.register(UserProfile)
#admin.site.register(Attends)
