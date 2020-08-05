from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile, User, Courses
# Create your views here.

def indexView(request):
    return render(request, 'index.html')

@login_required
def dashboardView(request):
    #Retrieves the users profile
    userId = request.user.id
    studentProfile = UserProfile.objects.get(user_id=userId)
    crsNotTaken = Courses.objects.exclude(userprofiles=studentProfile).all()
    #queryset with all of the users courses
    querySet = studentProfile.course.all()

    return render(request, 'dashboard.html', {'query_set':querySet,'crs_not_taken': crsNotTaken})


def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})

