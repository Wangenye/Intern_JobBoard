from django.db import models
from django.contrib.auth.models import  User
from  jobsApp.models import  Application
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class  UserProfile(models.Model):
    user = models.OneToOneField(User,related_name= 'userprofile',on_delete=models.CASCADE)
    is_employer = models.BooleanField(default=False)

User.userprofile = property(lambda u:UserProfile.objects.get_or_create(user=u)[0])

class ConversationMessage(models.Model):
    application = models.ForeignKey(Application,related_name='conversationmessage',on_delete=models.CASCADE)
    content = models.TextField()
    created_by = models.ForeignKey(User,related_name='conversationmessage',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
GENDER_CHOICES=[('Male','Male'),
         ('Female','Female')]
class UserDetail(models.Model):
    user = models.ForeignKey(User,related_name='userprofiledetails',on_delete=models.CASCADE,default=None)
    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    title = models.CharField(max_length=255,null=True)
    phone = models.CharField(max_length=14,null=True)
    # phone2 =  PhoneNumberField(null=True)
    country = CountryField(blank=True)
    role = models.CharField(max_length=255,null=True)
    gender = models.CharField(max_length=10,choices=[('Male','Male'),
         ('Female','Female')],null=True)

    def __str__(self):

        return self.first_name