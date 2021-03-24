from django.forms import ModelForm
from .models import UserDetail,CompanyDetail

class UserDetailForm(ModelForm):

    class Meta:
        model = UserDetail
        fields = ('first_name','gender','last_name','title','role','phone','country')


class CompanyDetailForm(ModelForm):

    class  Meta:

        model = CompanyDetail
        fields = ('company_name','company_ceo','company_about','company_website','company_logo','company_email','company_tel','company_country','company_city','company_location')