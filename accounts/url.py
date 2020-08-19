from django.urls import path, re_path
from . import views 
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('accounts/', views.indexView, name="home"),
    #restrict url below to prevent chances of bad url
    path('server/<course_title>', views.course_server, name="course_server"),
    path('dashboard/', views.dashboard_view, name="dashboard"),
    path('remove/', views.remove_view, name="remove"),
    path('login/', LoginView.as_view(), name="login_url"),
    path('register/', views.register_view, name="register_url"),
    path('logout/', LogoutView.as_view(next_page='dashboard'), name = "logout"),
]