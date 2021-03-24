from django.contrib import admin
from .models import UserProfile,UserDetail,CompanyDetail

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserDetail)
admin.site.register(CompanyDetail)
