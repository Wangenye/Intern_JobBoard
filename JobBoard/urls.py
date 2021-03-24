"""JobBoard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from JobBoard.UserProfileApp.views import UserDashboard
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from coreApp.views import  *
from jobsApp.views import  *
from UserProfileApp.views import  *
from django.contrib.auth import views 

urlpatterns = [
    path('', FrontPage,name='frontpage'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('login/',views.LoginView.as_view(template_name='coreApp/login.html'),name='login'),
    path('signup/', SignUp,name='signup'),
    path('admin/', admin.site.urls),
    # JobApp Urls
    path('jobs/',include('jobsApp.urls')),
    # User Profile Dashboard
    path('dashboard/',include('UserProfileApp.urls')),

    #Notifications
    path('notifications/',include('notificationApp.urls')),

   

]
