from django.urls import path,include
from .api import  api_search
from .views import *

urlpatterns = [
    path('api/search/',Search,name="api_search"),
    path('search/',Search,name="search"),
    # Adding new Job
    path('add/',AddJob,name='new'),
    # Job Details 
    path('<int:job_id>/',jobDetails,name='job_details'),
      path('<int:job_id>/edit',EditJob,name='edit_job'),
    # Applying for Job 
    path('<int:job_id>/apply_for_job/',apply_for_job,name='apply_for_job'),
]
