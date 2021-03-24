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
    jobseeker_image = models.ImageField(upload_to='Jobseeker/Images/',blank=True)
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

class  CompanyDetail(models.Model):
    user = models.ForeignKey(User,related_name='companydetails',on_delete=models.CASCADE,default=None)
    company_name = models.CharField(max_length=255,null=True)
    company_ceo = models.CharField(max_length=20,null=True)
    company_about = models.TextField(max_length=500,null=True)
    company_website= models.CharField(blank=True,max_length=100)
    company_logo = models.ImageField(upload_to='Employer/company_logos/')
    company_email = models.EmailField(blank=True)
    company_tel = models.CharField(blank=True,max_length=20)
    company_country = CountryField()
    company_city = models.CharField(max_length=30,blank=True)
    company_website= models.URLField(blank=True)
    company_location= models.URLField(blank=True)

    def __str__(self):

        return "Company Name : {} @ {}".format(self.company_name,self.company_city)
    

