from django.shortcuts import render,redirect
from .models import registration
from .models import login
from django.contrib import messages
from .models import complaint
from .models import Usm
from .models import uploadLecture
from .models import Enquiry
from .models import noti
from datetime import date
#from .models import 

# Create your views here.
#------------------------Methods for views---------------------------------------------------------
def layout(request):
    return render(request,'layout.html')

def home(request):
    return render(request, 'home.html')

def courses(request):
    return render(request, 'courses.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def About(request):
    return render(request, 'About.html')
    

def Reg(request):
    return render(request,'Registration.html')

def login(request):
    return render(request,'homelogin.html')


def Adminzone(request):
    return render(request, 'adminzone.html')

def Adminhome(request):
    return render (request , 'adminhome.html')
    
def showdata(request):
    return render (request , 'showdata.html')

def manageuser(request):
    ab = Registration.objects.all
    return render (request , 'showdata.html', {'show':ab})

def uploadstudy(request):
    return render(request,'uploadstudy.html')

def uploadassesment(request):
    return render(request,'uploadassesment.html')

def uploadlecture(request):
    return render(request, 'uploadlecture.html')

def updateprofile(request):
    return render(request, 'updateprofile.html')

def studenthome(request):
    return render(request,'studenthome.html')

def viewstudy(request):
    papaji=Usm.objects.all()
    return render(request, 'viewstudy.html',{'papaji':papaji})

def viewlecture(request):
    papaji=uploadLecture.objects.all()
    return render(request,'viewlecture.html',{'papaji':papaji})

def feedback(request):
    return render(request,'feedback.html')

def complaints(request):
    dg=registration.objects.all()
    return render(request,'complaintreg.html',{'dy':dg})


def enquiry(request):
    en=Enquiry.objects.all()
    return render(request,'enquiry.html', {'en':en})

def addnotification(request):
    return render(request,'addnotification.html')

def feedbackdata(request):
    return render(request,'feedbackdata.html')




#------------------------Methods for views---------------------------------------------------------

#====================================all save methods===========================================

def save(request):
    enrollmentno = request.POST['enrollmentno']
    name = request.POST['name']
    fname = request.POST['fname']
    mname = request.POST['mname']
    Gender = request.POST['Gender']
    address = request.POST['address']
    course = request.POST['course']
    branch = request.POST['branch']
    year = request.POST['year']
    mobile = request.POST['mobile']
    email = request.POST['email']
    password = request.POST['password']
    usertype = 'student'
    status = 'N'
    a=Registration(enrollmentno=enrollmentno,name=name,fname=fname,mname=mname,Gender=Gender,address=address,course=course,branch=branch,year=year,mobile=mobile,email=email,password=password)
    b = Login(userid=email,password=password,usertype=usertype,status=status)
    a.save()
    b.save()
    messages.success(request,'Your Registration is Successfully done .')
    return render(request,'Registration.html')


def logcode(request):
    if request.method=="POST":
       userid=request.POST['userid']
       password=request.POST['password']
       usertype=request.POST['usertype']
       ad = Login.objects.filter(userid=userid,password  =password).first()
       if ad:
         if ad.usertype=="student" and usertype=="student":
            request.session['userid'] = userid
            return redirect("adminportal")

         elif ad.usertype=="admin" and usertype=="admin":

            return redirect('adminzone')
         else:
            messages.success(request,'invalid user')
            return redirect('login')
       
       else:
           messages.success(request,'invalid user')
           return render(request,'homelogin')  

def adminportal(request):
    if 'userid' in request.session:
        return render (request,'adminlportal.html')
    else:
        return redirect('homelogin')
     


def complaintsave(request,id):
  if request.method == 'POST':
     sg=registration.objects.get(pk=id)
     subject=request.POST['subject']
     comp=reqeust.POST['comp']
     status='Pending'
     reqdate=date.today()
     v=complaint(id=id,name=sg.name,program=sg.course,branch=sg.branch,contactno=sg.mobile,email=sg.email,subject=subject,comp=comp,status=status,reqdate=reqdate)
     v.save()
     messages.success(request,'this complaint is registered')
     return redirect('complaints')




   


def Usmsave(request):
    program =request.POST['program']
    Branch =request.POST['Branch']
    Year =request.POST['Year']
    subject =request.POST['subject']
    file_name =request.POST['file_name']
    New_file =request.FILES['New_file']
    sv=Usm(program=program,Branch=Branch,Year=Year,subject=subject,file_name=file_name,New_file=New_file)
    sv.save()
    messages.success(request,'Usm is successfully uploaded')
    return redirect('uploadstudy')

def lecturesave(request):
    program=request.POST['program']
    Branch=request.POST['Branch']
    Year=request.POST['Year']
    Subject=request.POST['Subject']
    file_name=request.POST['file_name']
    Link=request.POST['Link']
    an=uploadLecture(program=program,Branch=Branch,Year=Year,Subject=Subject,file_name=file_name,Link=Link)
    an.save()
    messages.success(request,'your lectures are successfully uploaded')
    return redirect('uploadlecture')

def enqsave(request):
    name=request.POST['name']
    contactno=request.POST['contactno']
    email=request.POST['email']
    enq=request.POST['enq']
    enqdate=date.today()
    ens=Enquiry(name=name,contactno=contactno,email=email,enqdate=enqdate,)
    ens.save()
    message.success(request,'Enquery is saved')
    return redirect('contact')

def notisave(request):
    notim=request.POST['notim']
    notidate=date.today()
    ns=noti(notim=notim,notidate=notidate)
    ns.save()
    return redirect('addnotification')


#====================================all save methods===========================================