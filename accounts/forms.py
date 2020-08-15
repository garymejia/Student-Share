from django import forms
from .models import UserProfile, Course#, Attends


class CourseForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        self.courses=kwargs.pop('courses', None)
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['courses'].queryset = self.courses
