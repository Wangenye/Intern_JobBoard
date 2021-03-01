from django.shortcuts import redirect, render
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth import  login
from jobsApp.models import Job
from UserProfileApp.models import UserProfile

# Create your views here.


def FrontPage(request):
    jobs = Job.objects.filter(status=Job.ARCHIVED).order_by('-created_at')
    return render(request,'coreApp/froontpage.html',{'jobs':jobs})

def SignUp(request):
    # form = UserCreationForm()
    if request.method =='POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            account_type = request.POST.get('account_type','jobseeker')
            if account_type == 'employer':
                userprofile = UserProfile.objects.create(user=user,is_employer= True)
                # user.userprofile.is_employer =True
                userprofile.save()
            else:
                userprofile = UserProfile.objects.create(user=user,is_employer= False)
                # user.userprofile.is_employer =True
                userprofile.save()

            login(request,user)
            return redirect('dashboard')
        else:
            print("SignUp Form Error")
    else:
        form = UserCreationForm()
    return render(request,'coreApp/signup.html',{'form':form})
