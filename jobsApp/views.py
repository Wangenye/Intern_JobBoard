from django.shortcuts import redirect, render,get_object_or_404
from .models import Job
from .forms import AddJobForm,ApplicationJobForm
from django.contrib.auth.decorators import  login_required
from notificationApp.utilities import create_notification

# Create your views here.

def Search(request):
    return render(request,"jobsApp/search.html")


def jobDetails(request,job_id):
    job = Job.objects.get(pk=job_id)
    return render(request,'jobsApp/job_details.html',{'job':job,'userprofile':request.user.userprofile} )

@login_required
def apply_for_job(request,job_id):
    job = Job.objects.get(pk=job_id)

    if request.method == 'POST':
        form = ApplicationJobForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.created_by = request.user
            application.save() 

            create_notification(request,job.created_by,'application', extra_id=application.id)

            

            return redirect('dashboard')

    else:
        form = ApplicationJobForm()

    return render(request,'jobsApp/apply_job.html',{'form':form,'job':job,})


@login_required
def AddJob(request):
    if request.method =='POST':
        form = AddJobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()

            return redirect('dashboard')

    else:
         form = AddJobForm()

    return render(request,'jobsApp/add_job.html',{'form':form})

@login_required
def EditJob(request,job_id):
    job = get_object_or_404(Job,pk=job_id,created_by=request.user)
    if request.method =='POST':
        form = AddJobForm(request.POST or None,instance=job)

        if form.is_valid():
            job = form.save(commit=False)
            job.status = request.POST.get('status')
            job.save()

            return redirect('dashboard')

    else:
         form = AddJobForm(instance=job)

    return render(request,'jobsApp/edit_job.html',{'form':form,'job':job})