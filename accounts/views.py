from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required   
from django.http import Http404
from django.contrib.auth import get_user_model
from .models import UserProfile, Course#, Attends
from .forms import CourseForm

# Create your views here.

def indexView(request):
    return render(request, 'index.html')

@login_required
def dashboard_view(request):
    #Retrieves the users profile
    user_id = request.user.id
    #student_profile = UserProfile.objects.filter(user_id=user_id)
    
    #delete starting
    #student_profile = UserProfile.objects.filter(user_id)
    #DEFAULT MUST BE SET TO NONE OR SOMETHING. NEW USERS WILL HAVE AN ERROR BECAUSE THEY WONT HAVE A PROFILE
    student_profile = UserProfile.objects.filter(user_id=user_id)[0]
    enrolled_courses = student_profile.courses.all()
    all_courses = Course.objects.all()
    not_enrolled_courses = all_courses.difference(enrolled_courses)

    if request.method == 'POST':
        form = CourseForm(request.POST, courses=not_enrolled_courses)
        if form.is_valid():
            static_profile = UserProfile.objects.get(user=student_profile.user)
            static_profile.courses.add(*form['courses'].value())
        else:
            print(form.errors)
            raise Http404
    else:
        form = CourseForm(courses=not_enrolled_courses)
    return render(request, 'dashboard.html', {'enrolled_courses':enrolled_courses, 'form':form})

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})