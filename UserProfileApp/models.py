from django.db import models
from django.contrib.auth.models import  User
from  jobsApp.models import  Application

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
