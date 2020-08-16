from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required   
from django.http import Http404, HttpResponse
from django.contrib.auth import get_user_model
from django.urls import reverse
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

def remove_view(request):
    if request.method == "POST":
        info = request.POST['remove_value']
        #I want to make sure the user is enrolled in that course before i delete anything
        #im assuming im doing it wrong, any value passed to the database shouldnt be visible in html(i think) 
        #better way would be to pass the form through the form model. dont know how to do that so ill focus on it later
        try:
            student_profile = UserProfile.objects.filter(user_id=request.user.id)[0]
            user_profile = UserProfile.objects.get(user=student_profile.user)
            course = Course.objects.get(title = info)
            print(user_profile.courses.remove(course))
        except:
            print("Error unknown input from remove course")
    return redirect(reverse('dashboard'))


    #Work on how to properly redirect page in remove_view 
    #also should change dashboard view to redirect instead of render to prevent double post when user is filling out form with post and refreshed page