from django.db import models

# Create your models here.
class login(models.Model):
    userid=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=50)
    status=models.CharField(max_length=70)

class registration(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    enrollmentno = models.CharField(max_length=50)
    name = models.CharField(max_length=225)
    fname = models.CharField(max_length=225)
    mname = models.CharField(max_length=225)
    Gender = models.CharField(max_length=50)
    address = models.CharField(max_length=400)
    course = models.CharField(max_length=200)
    branch = models.CharField(max_length=300)
    year = models.IntegerField()
    mobile = models.IntegerField()
    email = models.CharField(max_length=400)
    password = models.CharField(max_length=100)
    New_file= models.ImageField(null=True)


class Usm(models.Model):
    id=models.IntegerField(primary_key=True ,auto_created=True)
    program=models.CharField(max_length=200)
    Branch=models.CharField(max_length=200)
    Year=models.CharField(max_length=20)
    subject=models.CharField(max_length=500)
    file_name=models.CharField(max_length=200)
    New_file=models.FileField(upload_to='myimage')

# class Assessment(models.Model):
#     id=models.IntegerField(primary_key=True ,auto_created=True)
#     program=models.CharField(max_length=200)
#     Branch=models.CharField(max_length=200)
#     Year=models.IntegerField()
#     Subject=models.CharField(max_length=500)
#     file_name=models.CharField(max_length=200)
#     New_file=models.FileField(upload_to='myimage')

class uploadLecture(models.Model):
    id=models.IntegerField(primary_key=True ,auto_created=True)
    program=models.CharField(max_length=200)
    Branch=models.CharField(max_length=200)
    Year=models.IntegerField()
    Subject=models.CharField(max_length=500)
    file_name=models.CharField(max_length=200)
    Link=models.CharField( max_length=100)

class complaint(models.Model):
    
    id=models.IntegerField(primary_key=True ,auto_created=True)
    name=models.CharField(max_length=300)
    program=models.CharField(max_length=300)
    branch=models.CharField(max_length=300)
    contact=models.IntegerField()
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=300)
    comp=models.CharField(max_length=10000)
    status=models.CharField(max_length=50)
    reqdate=models.DateTimeField()


class Feedback(models.Model):
    id=models.IntegerField(primary_key=True ,auto_created=True)
    name=models.CharField(max_length=300)
    program=models.CharField(max_length=300)
    branch=models.CharField(max_length=300)
    contact=models.IntegerField()
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=300)
    feed=models.CharField(max_length=10000)
    status=models.CharField(max_length=50)
    reqdate=models.DateTimeField()


# def Complaint(request):
#     sg=registration.objects.get(id)
#     id=request.POST['id']
#     subject=request.POST['id']
#     comp=request.POST['id']

class Enquiry(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=100)
    contactno=models.CharField(max_length=30)
    email=models.CharField(max_length=500)
    enq=models.CharField(max_length=1000)
    enqdate=models.DateTimeField()


class noti(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    notim=models.CharField(max_length=251)
    notidate=models.CharField(max_length=30)
    
    
