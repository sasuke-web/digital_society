from django.db import models
from Chairman.models import *

# Create your models here.

class House(models.Model):
    house_no = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    details = models.CharField(max_length=200)


    def __str__(self):
          return str(self.house_no)

class Member(models.Model):
    user_id = models.ForeignKey(User,on_delete=CASCADE)
    house_no = models.ForeignKey(House,on_delete=CASCADE)


    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    mobileno = models.CharField(max_length=30)

    job_specifications = models.CharField(max_length=50)
    job_address = models.TextField(max_length=500)
    birthdate = models.CharField(max_length=15)

    no_of_members = models.CharField(max_length=50)
    marrital_status = models.CharField(max_length=20)
    locality = models.CharField(max_length=100)
    nationality = models.CharField(max_length=15,default="Indian")
    gender = models.CharField(max_length=20)

    no_of_vehicles = models.CharField(max_length=100,default='')
    vehicle_type = models.CharField(max_length=100)
    id_proof = models.FileField(upload_to="media/documents/",default="media/default.png")
    profile_pic = models.FileField(upload_to="media/images/",default="media/default.png")


    def __str__(self):
        return self.firstname+" "+str(self.house_no.house_no)




class Notice(models.Model):
    # user_id = models.ForeignKey(User,on_delete=CASCADE)
    
    title= models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False)
    pic = models.FileField(upload_to="media/images/",null=True,blank=True)
    videofile = models.FileField(upload_to="media/videos/",null=True,verbose_name="video")
    

    def __str__(self):
        return self.title

    def NoticeViewCount(self):
        ncount = NoticeView.objects.filter(notice_id = self.id).count()

        if ncount>1:
            return str(ncount)+ " views"
        else:
            return str(ncount)+ " view"


    # m_id = models.ForeignKey(Member,on_delete=CASCADE)

class NoticeView(models.Model):
    notice_id = models.ForeignKey(Notice,on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)

    def __str__(self):
        return self.member_id.firstname+" "+self.notice_id.title

class Event(models.Model):
    # user_id = models.ForeignKey(User,on_delete=CASCADE)
    # house_no = models.ForeignKey(House,on_delete=CASCADE)

    
    title= models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False)
    pic = models.FileField(upload_to="media/images/",null=True,blank=True)
    videofile = models.FileField(upload_to="media/videos/",null=True,verbose_name="video")

class EventView(models.Model):
    event_id = models.ForeignKey(Event,on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)

    def __str__(self):
        return self.member_id.firstname+" "+self.event_id.title

class Complaint(models.Model):
    user_id = models.ForeignKey(User,on_delete=CASCADE)
    house_no = models.ForeignKey(House,on_delete=CASCADE)
    title= models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False)
    pic = models.FileField(upload_to="media/images/",null=True,blank=True)
    videofile = models.FileField(upload_to="media/videos/",null=True,verbose_name="video")
    is_solved = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id.firstname+" "+self.house_no
    