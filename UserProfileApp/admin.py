from django.contrib import admin
from .models import UserProfile,UserDetail

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserDetail)
