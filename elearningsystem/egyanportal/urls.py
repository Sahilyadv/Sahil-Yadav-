from django.urls import path
from .views import *
from  .import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [  
   path('', home, name="home"),
   path('homelogin',login,name="homelogin"),
   path('Reg',Reg,name="Reg"),
   path('layout', layout, name="layout"),
   path('About', About, name="About"),
   path('contact', contact, name="contact"),
   path('save', save, name="save"),
   path('logcode',logcode, name="logcode"),
   
   path('adminzone', Adminhome, name="adminzone"),
   #path('adminhome', Adminhome, name="adminhome"),
   path('showdata', manageuser, name="showdata"),
  path('uploadstudy', uploadstudy, name="uploadstudy"),
  path('uploadassesment',uploadassesment, name="uploadassesment"),
  path('uploadlecture', uploadlecture, name="uploadlecture"),
  path('adminportal',studenthome,name="adminportal"),
  path('updateprofile', updateprofile,name="updateprofile"),
  path('viewstudy',viewstudy,name="viewstudy"),
  path('viewlecture',viewlecture,name="viewlecture"),
  path('feedback',feedback,name="feedback"),
  path('complaintreg',complaints,name="complaintreg"),
  path('enquiry',enquiry,name="enquiry" ),
  path('addnotification',addnotification,name="addnotification"),
  path('Usm', Usm, name="Usm"),
  path('feedbackdata',feedbackdata,name="feedbackdata"),
  path('Usmsave', Usmsave, name="Usmsave"),
  path('lecturesave',lecturesave,name="lecturesave"),
  path('complaintsave/<int:id>',complaintsave,name="complaintsave"),
  path('enqsave',enqsave,name="enqsave"),
  path('notisave',notisave,name="notisave"),
  
 

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
