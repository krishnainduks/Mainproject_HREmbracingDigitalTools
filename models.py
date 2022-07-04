from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class add_mentor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='images/', null=True)
    department = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)

class add_trainee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mentorid = models.ForeignKey(add_mentor, on_delete=models.CASCADE,null=True)
    phone = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='images/', null=True)
    college =  models.CharField(max_length=100,null=True)
    designation = models.CharField(max_length=100,null=True)
    join_date= models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)
    status1 = models.CharField(max_length=100,null=True)

class time_table(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    mentorid = models.ForeignKey(add_mentor, on_delete=models.CASCADE,null=True)
    meeting_link= models.CharField(max_length=200,null=True)
    date= models.CharField(max_length=100,null=True)
    start_time= models.CharField(max_length=100,null=True)
    end_time= models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)

class Notification(models.Model):
    technology=  models.CharField(max_length=200,null=True)
    number= models.CharField(max_length=200,null=True)
    description= models.CharField(max_length=200,null=True)
    status = models.CharField(max_length=100,null=True)
    count= models.CharField(max_length=100,null=True)

class Certificate_Upload(models.Model):
    trainer= models.ForeignKey(add_trainee, on_delete=models.CASCADE,null=True)
    certificate = models.FileField('file/',null=True)
    date= models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)

class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    mentorid = models.ForeignKey(add_mentor, on_delete=models.CASCADE,null=True)
    meeting_link= models.CharField(max_length=200,null=True)
    date= models.CharField(max_length=100,null=True)
    start_time= models.CharField(max_length=100,null=True)
    end_time= models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)

class chat(models.Model):
    trainee = models.ForeignKey(add_trainee, on_delete=models.CASCADE, null=True)

    message = models.CharField(max_length=100,null=True)
    date = models.CharField(max_length=100,null=True)
    reply = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)












