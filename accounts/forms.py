from django import forms
from .models import UserProfile, Courses

class CourseForm(forms.Form):
    #Override forms init method to take an extra keyword argument, request
    def __init__(self, *args, **kwargs):
        self.crs = kwargs.pop('crs', None)
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields["crses"].queryset = forms.MultipleChoiceField(choices=self.crs)     
