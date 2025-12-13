from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete,pre_save,pre_delete,m2m_changed
#from django.core.signals import request_finished , request_started
# Create your models here.

class Profile (models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE) # on_delete = models.DO_NOTHING ,SET_NULL , ....
    phone = models.IntegerField(null=True ,blank=True)
    address = models.CharField(max_length=300,null=True ,blank=True)
    postalcode = models.IntegerField(null=True ,blank=True)

    def __str__(self):
        return self.user.username
def save_profile_user(sender ,**kwargs):
    if kwargs ['created'] : # create is boolean Ture or False
        user_profile = Profile(user = kwargs ['instance'])
        user_profile.save()
    else:
        pass

post_save.connect (sender= User ,receiver=save_profile_user)


class UserAddresses(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='addresses')
    title = models.CharField(max_length=50)  # مثلا "خانه"، "محل کار"
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    # می‌توانی فیلدهای بیشتری مثل شماره واحد، توضیحات و ... اضافه کنی

    def __str__(self):
        return f"{self.profile} -{self.title} - {self.city}"