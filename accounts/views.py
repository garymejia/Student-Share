from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Courses
from django.http import HttpResponseRedirect

# Create your views here.

def indexView(request):
    return render(request, 'index.html')

@login_required
def dashboard_view(request):
    #Retrieves the users profile
    user_id = request.user.id
    student_profile = UserProfile.objects.get(user_id=user_id)
    crs_not_taken = Courses.objects.exclude(userprofiles=student_profile).all()
    #queryset with all of the users courses
    query_set = student_profile.course.all()

    return render(request, 'dashboard.html', {'query_set':query_set, 'crs_not_taken': crs_not_taken})

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})