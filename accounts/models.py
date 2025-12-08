from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile (models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE) # on_delete = models.DO_NOTHING ,SET_NULL , ....
    phone = models.IntegerField(null=True ,blank=True)
    address = models.CharField(max_length=300,null=True ,blank=True)
    postalcode = models.IntegerField(null=True ,blank=True)