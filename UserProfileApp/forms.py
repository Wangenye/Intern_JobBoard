from django.forms import ModelForm
from .models import UserDetail

class UserDetailForm(ModelForm):

    class Meta:
        model = UserDetail
        fields = ('first_name','gender','last_name','title','role','phone','country')