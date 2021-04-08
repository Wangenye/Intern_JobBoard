from django.forms import ModelForm
from .models import UserDetail,CompanyProfile,JustFormation

class UserDetailForm(ModelForm):

    class Meta:
        model = UserDetail
        fields = ('first_name','gender','last_name','title','role','phone','country')




class CompanyProfileForm(ModelForm):

    class Meta:
        model =CompanyProfile
        fields = ('company_name','company_ceo','company_about','company_logo','company_email','company_tel','company_country','company_city','company_website','company_location')

class JustFormForm(ModelForm):

    class Meta:
        model = JustFormation

        fields =('company_name','company_ceo','company_about','company_website','company_logo')
