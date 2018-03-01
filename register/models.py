from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User)

    protfolio_pic = models.ImageField(upload_to='profile_pics',null = True,blank= True);

    protfolio_site = models.URLField(null=True,blank=True)

    # put the options ,i,e few names of colleges here
    currently_pursuing = models.IntegerField(blank=False,null=False)

    School = models.CharField(blank=False,null=False,max_length=200)

    #put the number of options available for quizzes here
    interested_areas = models.CharField(null=False,blank=False)


    def __str__(self):
        return self.username
