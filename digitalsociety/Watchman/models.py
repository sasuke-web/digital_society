from django.db import models
from Chairman.models import *

# Create your models here.

class WatchMan(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname =models.CharField(max_length=50)
    contact = models.CharField(max_length=13)
    id_proof = models.FileField(upload_to="media/images",default="media/default.png")
    profile_pic = models.FileField(upload_to="media/images",default="media/default.png")

    def __str__(self):
        return self.firstname