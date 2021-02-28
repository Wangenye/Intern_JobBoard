from django import forms

from .models import  Job,Application

class  AddJobForm(forms.ModelForm):

    class Meta:
        model =Job
        fields = ['title','show_description','long_description','company_name','company_address','company_zipcode','company_place','company_country']

class  ApplicationJobForm(forms.ModelForm):

    class Meta:
        model =Application
        fields = ['content','experiences']