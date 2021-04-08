from django.contrib import admin
from .models import UserProfile,UserDetail,CompanyProfile,JustFormation

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserDetail)
admin.site.register(JustFormation)
admin.site.register(CompanyProfile)
