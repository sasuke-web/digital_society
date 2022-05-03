import email
from django.shortcuts import render,redirect
from Chairman.models import *
from Member.models import *
# Create your views here.

def m_profile(request):
      
            
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        
        if request.POST:
                currentpassword=request.POST['currentpassword']
                newpassword=request.POST['newpassword']

                if uid.password == currentpassword:
                    uid.password =newpassword
                    uid.save()
                    return redirect('m_profile')
        
        else:
                if uid.role == "Member" or "member":
                    mid = Member.objects.get(user_id=uid)
                    return render(request,"Member\m_profile.html",{'uid': uid,'mid':mid})


def m_dashboard(request):
    return redirect('login')

def m_all_members(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role == "Member" or "member":
            mid = Member.objects.get(user_id=uid)
            m_all = Member.objects.exclude(user_id=uid)
            return render(request,"Member/m_all_members.html",{'uid':uid,'mid':mid,'m_all':m_all})


def m_all_notice(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        mid = Member.objects.get(user_id = uid)
        n_all = Notice.objects.all()

        return render(request,"Member/m_all_notice.html",{'uid':uid,'mid':mid,'n_all':n_all})
    else:
        return redirect('login')

def m_all_notice_details(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        mid = Member.objects.get(user_id = uid)
        nid = Notice.objects.get(id=pk)
        nall = NoticeView.objects.filter(notice_id =nid,member_id=mid)
        if nall:
            print("Already viewed")
        else:
            print("First View by member")
            nvid = NoticeView.objects.create(notice_id =nid,member_id=mid)
        return render(request,"Member/m_all_notice_details.html",{'uid':uid,'mid':mid,'nid':nid})
    else:
        return redirect('login')

def m_add_complaint(request):
    if request.POST:
        house_all = House.objects.all()
        house_no = request.POST.get('house_no')
        hid = House.objects.get(house_no= house_no)
        uid = User.objects.get(email=request.session['email'])
        if "pic" in request.FILES and "videofile" not in request.FILES:
                coid = Complaint.objects.create(
                    user_id = uid,
                    house_no = hid,
                    title = request.POST['title'],
                    description = request.POST['description'],
                    pic = request.FILES['pic'],
                    # videofile =request.FILES['videofile']
                
                )
        elif "videofile" in request.FILES and "pic" not in request.FILES:
                coid = Complaint.objects.create(
                    user_id = uid,
                    house_no = hid,
                    title = request.POST['title'],
                    description = request.POST['description'],
                    # pic = request.FILES['pic'],
                    videofile = request.FILES['videofile']
                
                )
        
        elif "pic" and "videofile" in request.FILES:
                coid = Complaint.objects.create(
                    user_id = uid,
                    house_no = hid,
                    title = request.POST['title'],
                    description = request.POST['description'],
                    pic = request.FILES['pic'],
                    videofile = request.FILES['videofile']
                
                )
                
        else:
                house_all = House.objects.all()
                house_no = request.POST.get('house_no')
                hid = House.objects.get(house_no= house_no)
                
                
                coid = Complaint.objects.create(
                    user_id = uid,
                    house_no = hid,
                    title = request.POST['title'],
                    description = request.POST['description'],
                    # pic = request.FILES['pic'],
                    # videofile =request.FILES['videofile']
                
                )
        return redirect("m-all-complaint")
    else:
        house_all = House.objects.all()
        uid = User.objects.get(email=request.session['email'])
        mid = Member.objects.get(user_id = uid)
        return render(request,"Member/m_add_complaint.html",{'uid':uid,'mid':mid,'house_all':house_all})

def m_all_complaint(request):
    if "email" in request.session:
            uid =User.objects.get(email=request.session['email'])
            # mid = Member.objects.all()
            mid = Member.objects.get(user_id=uid)
            coall = Complaint.objects.all()
            return render(request,"Member/m_all_complaints.html",{'uid':uid,'mid':mid,'coall':coall}) 
    # if "email" in request.session:
    #     house_no = request.POST.get('house_no')
    #     hid = House.objects.get(house_no= house_no)
    #     uid = User.objects.get(email=request.session['email'])
    #     mid = Member.objects.get(user_id = uid)
    #     co_all = Complaint.objects.all()

        # return render(request,"Member/m_all_complaints.html",{'uid':uid,'mid':mid,'co_all':co_all,'hid':hid})
    else:
        return redirect('login')

def m_add_event(request):
    if request.POST:
        if "pic" in request.FILES and "video" not in request.FILES:
                eid = Event.objects.create(
                    # user_id = uid,
                    # house_no = hid,

                    title = request.POST['title'],
                    description = request.POST['description'],
                    pic = request.FILES['pic'],
                    # videofile =request.FILES['videofile']
                
                )
        elif "video" in request.FILES and "pic" not in request.FILES:
                eid = Event.objects.create(
                    # user_id = uid,
                    # house_no = hid,

                    title = request.POST['title'],
                    description = request.POST['description'],
                    # pic = request.FILES['pic'],
                    video = request.FILES['videofile']
                
                )

        elif "pic" and "video" in request.FILES:
                eid = Event.objects.create(
                    # user_id = uid,
                    # house_no = hid,

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
        return redirect("m-all-event")
    else:
        uid = User.objects.get(email=request.session['email'])
        mid = Member.objects.get(user_id = uid)
        return render(request,"Member/m_add_event.html",{'uid':uid,'mid':mid})

def m_all_event(request):
      if "email" in request.session:
            uid =User.objects.get(email=request.session['email'])
            # mid = Member.objects.all()
            # house_id = request.POST.get('house_no')
            # hid = House.objects.get(house_id= house_id)

            mid = Member.objects.get(user_id=uid)
            eall = Event.objects.all().order_by('created_at').reverse()
            return render(request,"Member/m_event_list.html",{'uid':uid,'mid':mid,'eall':eall})
