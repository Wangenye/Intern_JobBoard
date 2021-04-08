from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from jobsApp.models import Job,Application
from UserProfileApp.models import ConversationMessage
from notificationApp.utilities import create_notification
from .forms import  UserDetailForm,JustFormForm

# Create your views here.
@login_required
def UserDashboard(request):
    if request.method =="POST":
        jobseeker_form = UserDetailForm(request.POST)
        if jobseeker_form.is_valid():
            profiledetails =jobseeker_form.save(commit=False)
            profiledetails.user = request.user
            profiledetails.save()
        else:
            print("User Form Error")
    else:
        jobseeker_form = UserDetailForm(prefix='jobseeker_form')



    jobs = Job.objects.all()
    return render(request,'UserProfileApp/dashboard.html',{'userprofile':request.user.userprofile,'jobs':jobs,'jobseeker_form':jobseeker_form,})

@login_required
def CompanyProfileUpdater(request):

    if request.method == 'POST':
        form =  JustFormForm(request.POST)
        if form.is_valid():
            companyProfile = form.save(commit=False)
            companyProfile.post = request.user
            companyProfile.save()

            return redirect('dashboard')
        else:
            print("Error C")
    else:
        form =  JustFormForm(prefix='form')


    return render(request,'UserProfileApp/company_profile.html',{'userprofile':request.user.userprofile,'form':form})


@login_required
def view_application(request,application_id):
    if request.user.userprofile.is_employer:
        application = get_object_or_404(Application,pk=application_id,job__created_by=request.user)
    else:
        application = get_object_or_404(Application,pk=application_id,created_by=request.user)

    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            conversationmessage = ConversationMessage.objects.create(application= application,content=content,created_by=request.user)
            create_notification(request,application.created_by,'message', extra_id=application.id)
            return redirect('view_application',application_id = application_id)

    return render(request,'UserProfileApp/view_application.html',{'application':application})

@login_required
def view_dashboard_job(request,job_id):
    job =  get_object_or_404(Job,pk=job_id,created_by=request.user)
    return render(request,'UserProfileApp/view_dashboard_job.html',{'job':job})
