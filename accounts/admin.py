from django.contrib import admin
from .models import Course, UserProfile, Document
# Register your models here.

admin.site.register(Course)
admin.site.register(Document)
admin.site.register(UserProfile)
#admin.site.register(Attends)
