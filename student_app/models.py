from django.db import models

# Create your models here.

class login(models.Model):
    login_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100)

class staff(models.Model):
    staff_id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    login=models.ForeignKey(login,on_delete=models.CASCADE)

class course(models.Model):
    course_id=models.AutoField(primary_key=True)
    course=models.CharField(max_length=100)
    
class parent(models.Model):
    parent_id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    
class student(models.Model):
    student_id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    parent=models.ForeignKey(parent,on_delete=models.CASCADE)
    


class attendance(models.Model):
    attendance_id=models.AutoField(primary_key=True)
    attendance=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    student=models.ForeignKey(student,on_delete=models.CASCADE)



class subject(models.Model):
    subject_id=models.AutoField(primary_key=True)
    subject=models.CharField(max_length=100)
    course=models.ForeignKey(course,on_delete=models.CASCADE)

class feedback(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    feedback=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    user_id=models.IntegerField(max_length=100)

class leave(models.Model):
    leave_id=models.AutoField(primary_key=True)
    sendby=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    send_id=models.IntegerField(max_length=100)


class upload(models.Model):
    file_id=models.AutoField(primary_key=True)

    file=models.FileField()

class result(models.Model):
    result_id=models.AutoField(primary_key=True)
    marks=models.IntegerField(max_length=100)
    subject=models.ForeignKey(subject,on_delete=models.CASCADE)
    student=models.ForeignKey(student,on_delete=models.CASCADE)

class notice(models.Model):
    notice_id=models.AutoField(primary_key=True)
    notice=models.CharField(max_length=100)
    student=models.ForeignKey(student,on_delete=models.CASCADE)



class sandeep(models.Model):
    img_id=models.AutoField(primary_key=True)
    img_name=models.FileField()




