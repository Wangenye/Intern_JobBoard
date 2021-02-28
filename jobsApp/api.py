import json

from django.db.models import  Q
from django.http import  JsonResponse

from .models import  Job

def api_search(request):

    jobslists = []
    data=json.loads(request.body)
    query = data['query']
    company_location = data['company_location']

    jobs = Job.objects.filter(Q(title__icontains=query) | Q(show_description__icontains=query) | Q(long_description__icontains=query) | Q(company_name__icontains=query) | Q(company_place__icontains=query))
    if company_location:
        jobs = jobs.filter(company_location = company_location)

    for job in jobs:
        obj ={
            'id':job.id,
            'title':job.title,
            'company_name':job.company_name,
            'url':'/jobs/%s/'%job.id
        }

        jobslists.append(obj)

    
    return JsonResponse({'jobs': jobslists})