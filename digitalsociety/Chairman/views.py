# from email.message import EmailMessage
# from logging import exception
# from random import randint,choice
# import re
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import *
# from django.core.mail import send_mail
# from Member.models import *


# Create your views here.
from asyncio import events
import email
from secrets import choice
from urllib.request import Request
import django
from django.shortcuts import render, redirect

from .models import *
from django.core.mail import send_mail
from random import randint
from django.views.decorators.csrf import csrf_exempt
from Member.models import *
from Watchman.models import *
 
# Create your views here.

def home(request):
    return render(request,"Chairman\index.html")

def login(request):
      if "email" in request.session:
            house_no = request.POST.get('house_no')
            uid = User.objects.get(email= request.session ['email'])
            nall = Notice.objects.all().order_by('created_at').reverse()
            if uid.role=='Chairman':
                  cid = Chairman.objects.get(user_id = uid)
                  mid = Member.objects.all()
                  # hid = House.objects.get(house_no= house_no)
                  # hid=house_no
                  mcount=Member.objects.all().count()
                  ncount= Notice.objects.all().count()
                  ecount = Event.objects.all().count()
                  return render(request,"Chairman/index.html", {'uid':uid, 'cid':cid,'mid':mid,'mcount':mcount,'nall':nall,'ncount':ncount,'ecount':ecount})
            elif uid.role == "member" or "Member":
                  mid = Member.objects.get(user_id = uid)
                  mcount=Member.objects.all().count()
                  ncount= Notice.objects.all().count()
                  ecount = Event.objects.all().count()
                  return render(request,"Member/m_index.html", {'uid':uid, 'mid':mid,'mcount':mcount,'nall':nall,'ncount':ncount,'ecount':ecount})
      else:
            pass
            # e_msg= "Email doesn't exist"  
            # return render(request,"Chairman/login.html",{'e_msg':e_msg})
   
      if request.POST:
        pemail=request.POST['email']
        ppassword=request.POST['password']

    
    #here User is modelname, email is the fieldname and pemail is python variable which contains html input
    #(variable=modelname.objects.get(fieldame,python_variable))
      try:
            uid = User.objects.get(email= pemail)  
            if uid:
                  if uid.password== ppassword: 

                        if uid.role=="Chairman":
                              cid = Chairman.objects.get(user_id = uid)
                              request.session['email']=uid.email
                              send_mail(" Digital Society","WELCOME TO THE DIGITAL SOCIETY","testerhariom50@gmail.com",[uid.email])
                              return render(request,"Chairman\index.html", {'uid':uid, 'cid':cid})

                        elif uid.role=="member" or "Member":

                              mid=Member.objects.get(user_id=uid)

                              if uid.first_time_login==False:
                                    email=uid.email
                                    otp=randint(1111,9999)
                                    uid.otp=otp
                                    uid.save()
                                    msg= "you otp is "+str(otp)
                                    send_mail("Forgot-password",msg,"testerhariom50@gmail.com",[email])
                                    return render(request,"Member\m_reset-password.html",{'email':email})

                              else:

                                    uid = User.objects.get(email= pemail)
                                    mid = Member.objects.get(user_id = uid)
                                    request.session['email']=uid.email
                        
                                    return render (request, "Member/m_index.html",{'uid':uid,'mid':mid})
                  
                  else:

                        e_msg="Invalid password"
                        return render(request,"Chairman\login.html",{'e_msg':e_msg})
      except:
            e_msg= "Email doesn't exist"  
            return render(request,"Chairman\login.html",{'e_msg':e_msg})
                   

      else:
            return render(request, "Chairman\login.html")

def logout(request):
    if "email" in request.session:
            del request.session['email']
            s_msg="Successfully Logged out"
            return render(request,"Chairman\login.html",{'s_msg':s_msg})
        
    else:
        return render(request,"Chairman\login.html")



# def home(request):
#       return render(request,"Chairman\index.html")

# def login(request):
#       # if "email" in request.session:
#       #       uid = User.objects.get(email=request.session['email'])
#       #       if uid.role == "Chairman": #or "chairman":
#       #            cid = Chairman.objects.get(user_id=uid)
#       #            print("================================================")
#       #            return render(request,"Chairman\index.html",{'uid': uid,'cid':cid})
#       #       else:
#       #             print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
#       #             return render(request,"Chairman\login.html")
                  
      
#       if request.method == "POST":
#             print("===============inpost")
#             pemail = request.POST['email']
#             ppassword = request.POST['password']
            
            
#             uid = User.objects.get(email=pemail)
            
#             # if uid:
            
#             if uid.password == ppassword:
                 
#                   if uid.role == "member":
#                         print("77777777777777777777777")
#                         mid = Member.objects.get(user_id = uid)
#                         if uid.first_time_login == False:
#                               print("-------->",mid)
                                    
                                    
#                               email= uid.email
#                               otp =randint(1111,9999)
#                               uid.otp = otp
#                               uid.save()
#                               msg = "your otp is"+str(otp)
#                               send_mail("Password Reset",msg,"10maypython@gmail.com",[email])
#                               return render(request,"Member\m_reset-password.html",{'email':email})
#                               print("............", mid)
                  
#                   elif uid.role == "chairman" or "Chairman":
#                         print("chirman                       =============================")
#                         cid = Chairman.objects.get(user_id=uid)
#                         request.session['email'] = uid.email
#                         send_mail("Black Label Society","Welcome","10maypython@gmail.com",[uid.email])
#                         return render(request,"Chairman\index.html",{'uid': uid,'cid':cid})
#                   else:
#                         # mid = Member.objects.get(user_id = uid)
#                         return render(request,"Chairman\login.html",{'uid': uid,'mid':mid})
#             else:
#                   print("===================================----------ggggggggggg==================")
#                   return render(request,"Chairman\login.html")            
#       else:
#             return render(request,"Chairman\login.html")

          
      

# def logout(request):
#       try:
#             del request.session["email"]
#       except:
#             pass
#       return render(request,'Chairman/login.html')
            

def c_profile(request):
      
            
      if "email" in request.session:
            uid = User.objects.get(email=request.session['email'])
            
            if request.POST:
                  currentpassword=request.POST['currentpassword']
                  newpassword=request.POST['newpassword']

                  if uid.password == currentpassword:
                        uid.password =newpassword
                        uid.save()
                        return redirect('c-profile')
            
            else:
                  if uid.role == "Chairman":
                        cid = Chairman.objects.get(user_id=uid)
                        return render(request,"Chairman\c_profile.html",{'uid': uid,'cid':cid})

      
      else:
            redirect('login')

def c_dashboard(request):
      return redirect('login')

def forgot_password(request):
      if request.POST:
            email = request.POST['email']
            otp =randint(1111,9999)
            uid = User.objects.get(email=email)
            try:
                  if uid:
                        uid.otp = otp
                        uid.save()
                        msg = "your otp is"+str(otp)
                        send_mail("Password Reset",msg,"10maypython@gmail.com",[email])
                        return render(request,"Chairman/reset-password.html",{'email': email})

            except:
                  e_msg = 'email does not exist'
                  return render(request,"Chairman/reset-password.html",{'email': email})
                  #return render(request,"Chairman/forgotpassword.html",{'e_msg':e_msg})
      else:
            return render(request,"Chairman/forgotpassword.html")

def reset_password(request):
      if request.POST:
            email = request.POST['email']
            otp = request.POST['otp']
            newpassword = request.POST['newpassword']
            confirmpassword = request.POST['confirmpassword']

            uid = User.objects.get(email=email)

            if newpassword == confirmpassword:
                  if str(uid.otp) == otp and uid.email == email:
                       uid.password =newpassword
                       uid.is_verified = True
                       uid.first_time_login = True
                       uid.save()
                       return redirect('login')
                  else:
                        e_msg= "Invalid OTP" 
                        return render(request,"Chairman/reset-password.html",{'e_msg':e_msg,'email': email})


            else:
                  e_msg= "Password does not match"
                  return render(request,"Chairman/reset-password.html",{'e_msg':e_msg,'email': email})
      else:
            return redirect('forgot-password')

def add_member(request):
      if "email" in request.session:
            uid =User.objects.get(email=request.session['email'])
            cid = Chairman.objects.get(user_id = uid)
            l1 = ["ass246","ad466","sgff78","5466ddad"]
            if request.POST:
                  email = request.POST['email']
                  password = choice(l1)
                  house_no = request.POST.get('house_no')
                  role = "member"

                  

                  uid = User.objects.create(email=email,password=password,role=role)
                  hid = House.objects.get(house_no= house_no)
                  hid.status = "Active"
                  hid.save()
                  
                  print("---------UID",uid)
                  mid = Member.objects.create(
                              user_id = uid,
                              house_no = hid,
                  
                              firstname = request.POST['firstname'],
                              lastname = request.POST['lastname'],
                              mobileno = request.POST['mobileno'],
                              job_specifications = request.POST['job_specifications'],
                              birthdate = request.POST['birthdate'],
                              job_address = request.POST['job_address'],

                              no_of_members = request.POST['no_of_members'],
                              marrital_status = request.POST['marrital_status'],
                              locality = request.POST['locality'],
                              nationality = request.POST['nationality'],
                              gender = request.POST['gender'],
                              no_of_vehicles= request.POST['no_of_vehicles'],
                              vehicle_type = request.POST['vehicle_type'],

                              id_proof = request.FILES['id_proof'],
                  )
                  if mid:
                        msg = "your password is"+password
                        send_mail("Welcome to Black Label Society",msg,"10maypython@gmail.com",[email])
                  mid = Member.objects.all()   
                  return render(request,"Chairman/all-members.html",{'uid':uid,'cid':cid,'mid':mid})

                  
            else:
                  house_all = House.objects.filter(status = "pending")
            

                  return render(request,"Chairman/add-member.html",{'uid':uid,'cid':cid,'house_all':house_all})

      else:
            return redirect('login')

def all_members(request):
      
      if "email" in request.session:
            uid =User.objects.get(email=request.session['email'])
            mid = Member.objects.all()
            cid = Chairman.objects.get(user_id=uid)

            if uid.role == "Chairman" or "chairman":
                  
                  return render(request,"Chairman/all-members.html",{'uid':uid,'cid':cid,'mid':mid})
            
            elif uid.role == "Member" or "member":
                  # mid = Member.objects.all()
                  # cid = Chairman.objects.all()

                  return render(request,"Member/m_all_members.html",{'uid':uid,'cid':cid,'mid':mid})
      
def add_notice(request):
      if request.POST:
            if "pic" in request.FILES and "video" not in request.FILES:
                  nid = Notice.objects.create(

                        title = request.POST['title'],
                        description = request.POST['description'],
                        pic = request.FILES['pic'],
                        # videofile =request.FILES['videofile']
                  
                  )
            elif "video" in request.FILES and "pic" not in request.FILES:
                  nid = Notice.objects.create(

                        title = request.POST['title'],
                        description = request.POST['description'],
                        # pic = request.FILES['pic'],
                        video = request.FILES['videofile']
                  
                  )
            
            elif "pic" and "video" in request.FILES:
                  nid = Notice.objects.create(

                        title = request.POST['title'],
                        description = request.POST['description'],
                        pic = request.FILES['pic'],
                        video = request.FILES['video']
                  
                  )
                  
            else:
                  nid = Notice.objects.create(

                        title = request.POST['title'],
                        description = request.POST['description'],
                        # pic = request.FILES['pic'],
                        # videofile =request.FILES['videofile']
                  
                  )
            return redirect("all-notice")
      else:
            uid = User.objects.get(email=request.session['email'])
            cid = Chairman.objects.get(user_id = uid)
            return render(request,"Chairman/add-notice.html",{'uid':uid,'cid':cid})


def all_watchman(request):
      if "email" in request.session:
            uid =User.objects.get(email=request.session['email'])
            # mid = Member.objects.all()
            cid = Chairman.objects.get(user_id=uid)
            wall = WatchMan.objects.all()
            return render(request,"Chairman/all-watchman.html",{'uid':uid,'cid':cid,'wall':wall}) 

def approved(request,pk):
      if "email" in request.session:
            uid =User.objects.get(email=request.session['email'])
            # mid = Member.objects.all()
            cid = Chairman.objects.get(user_id=uid)
            user_id = User.objects.get(id = pk)
            user_id.is_verified = True
            user_id.save()
            # wid = WatchMan.objects.all()
            return redirect('all-watchman')
def rejected(request,pk):
      if "email" in request.session:
            uid =User.objects.get(email=request.session['email'])
            # mid = Member.objects.all()
            cid = Chairman.objects.get(user_id=uid)
            user_id = User.objects.get(id = pk)
            user_id.is_verified = False
            user_id.save()
            # wid = WatchMan.objects.all()
            return redirect('all-watchman')

def all_notice(request):
      if "email" in request.session:
            uid =User.objects.get(email=request.session['email'])
            # mid = Member.objects.all()
            cid = Chairman.objects.get(user_id=uid)
            nall = Notice.objects.all().order_by('created_at').reverse()
            return render(request,"Chairman/notice-list.html",{'uid':uid,'cid':cid,'nall':nall})

def del_notice(request,pk):
      if "email" in request.session:
            uid =User.objects.get(email=request.session['email'])
            # mid = Member.objects.all()
            cid = Chairman.objects.get(user_id=uid)
            nid = Notice.objects.get(id= pk)
            nid.delete()
            nall = Notice.objects.all().order_by('created_at').reverse()
            return redirect('all-notice')

      else:
            return redirect('login')

def noticeview_details(request,pk):
      if "email" in request.session:
            uid = User.objects.get(email=request.session['email'])
            cid = Chairman.objects.get(user_id=uid)
            print("---> pk ",pk)
            nid = Notice.objects.get(id = pk)
            nvid = NoticeView.objects.filter(notice_id = nid)
            
            return render(request,"Chairman/noticeview-details.html",{'uid':uid,'cid':cid,'nid':nid,'nvid':nvid})
            # return redirect('all-notice')

      else:
            return redirect('login')

def add_event(request):
      if request.POST:
            if "pic" in request.FILES and "video" not in request.FILES:
                  eid = Event.objects.create(

                        title = request.POST['title'],
                        description = request.POST['description'],
                        pic = request.FILES['pic'],
                        # videofile =request.FILES['videofile']
                  
                  )
            elif "video" in request.FILES and "pic" not in request.FILES:
                  eid = Event.objects.create(

                        title = request.POST['title'],
                        description = request.POST['description'],
                        # pic = request.FILES['pic'],
                        video = request.FILES['videofile']
                  
                  )
            
            elif "pic" and "video" in request.FILES:
                  eid = Event.objects.create(

                        title = request.POST['title'],
                        description = request.POST['description'],
                        pic = request.FILES['pic'],
                        video = request.FILES['video']
                  
                  )
                  
            else:
                  eid = Event.objects.create(

                        title = request.POST['title'],
                        description = request.POST['description'],
                        # pic = request.FILES['pic'],
                        # videofile =request.FILES['videofile']
                  
                  )
            return redirect("all-event")
      else:
            uid = User.objects.get(email=request.session['email'])
            cid = Chairman.objects.get(user_id = uid)
            return render(request,"Chairman/add-event.html",{'uid':uid,'cid':cid})

def all_event(request):
      if "email" in request.session:
            uid =User.objects.get(email=request.session['email'])
            # mid = Member.objects.all()
            cid = Chairman.objects.get(user_id=uid)
            eall = Event.objects.all().order_by('created_at').reverse()
            return render(request,"Chairman/event-list.html",{'uid':uid,'cid':cid,'eall':eall})

def del_event(request,pk):
      if "email" in request.session:
            uid =User.objects.get(email=request.session['email'])
            # mid = Member.objects.all()
            cid = Chairman.objects.get(user_id=uid)
            eid = Event.objects.get(id= pk)
            eid.delete()
            eall = Event.objects.all().order_by('created_at').reverse()
            return redirect('all-event')

def eventview_details(request,pk):
      if "email" in request.session:
            uid = User.objects.get(email=request.session['email'])
            cid = Chairman.objects.get(user_id=uid)
            eid = Event.objects.get(id = pk)
            evid = EventView.objects.filter(event_id = eid)
            
            return render(request,"Chairman/eventview-details.html",{'uid':uid,'cid':cid,'eid':eid,'evid':evid})

def all_complaint(request):
      if "email" in request.session:
            uid =User.objects.get(email=request.session['email'])
            mid = Member.objects.all()
            cid = Chairman.objects.get(user_id=uid)
            co_all = Complaint.objects.all()
            house_all = House.objects.all()
            return render(request,"Chairman/complaint-list.html",{'uid':uid,'cid':cid,'mid':mid,'co_all':co_all,'house_all':house_all}) 

def c_approved(request,pk):
      if "email" in request.session:
            uid =User.objects.get(email=request.session['email'])
            # mid = Member.objects.all()
            cid = Chairman.objects.get(user_id=uid)
            user_id = User.objects.get(id = pk)
            com_id = Complaint.objects.all()
            com_id.is_solved = True
            com_id.update()
            # wid = WatchMan.objects.all()
            return redirect('all-complaint')
def pending(request,pk):
      if "email" in request.session:
            uid =User.objects.get(email=request.session['email'])
            # mid = Member.objects.all()
            cid = Chairman.objects.get(user_id=uid)
            user_id = User.objects.get(id = pk)
            com_id = Complaint.objects.all()
            com_id.is_solved = False
            com_id.update()
            # wid = WatchMan.objects.all()
            return redirect('all-complaint')