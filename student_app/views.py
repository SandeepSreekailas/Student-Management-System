from django.shortcuts import render,HttpResponse

# Create your views here.
from student_app.models import *
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request,"home.html")

def adhome(request):
    return render(request,"adminhome.html")

def sthome(request):
    return render(request,"staffhome.html")

def stuhome(request):
    return render(request,"studenthome.html")

def prnthome(request):
    return render(request,"parenthome.html")

def logins(request):
    if request.method=='POST':
        uname=request.POST['user']
        passw=request.POST['passw']

        try:

            a=login.objects.get(username=uname,password=passw)
            if a:
                utype=a.usertype
                request.session['lid']=a.pk

                print("////",request.session['lid'])

                if utype=='admin':
                    return HttpResponse("<script>alert('Login Successful');window.location='/adminhome';</script>")
                elif utype=='staff':
                    g=staff.objects.get(login_id=request.session['lid'])
                    request.session['stid']=g.pk

                    return HttpResponse("<script>alert('Login Successful');window.location='/staffhome';</script>") 
                elif utype=='student':
                    f=student.objects.get(login_id=request.session['lid'])
                    request.session['sid']=f.pk

                    print(request.session['sid'],"////////////////")
                    
                    return HttpResponse("<script>alert('Login Successful');window.location='/studenthome';</script>") 
                elif utype=='parent':
                    i=parent.objects.get(login_id=request.session['lid'])
                    request.session['pid']=i.pk

                    return HttpResponse("<script>alert('Login Successful');window.location='/parenthome';</script>") 
                else:
                    return HttpResponse("<script>alert('invalid user');window.location='/login';</script>")
        except:
            return HttpResponse("<script>alert('invalid user');window.location='/login';</script>") 
                    


    return render(request,"login.html")

def staffreg(request):
     if request.method=='POST':
          fname=request.POST['fname']
          lname=request.POST['lname']
          place=request.POST['place']
          phone=request.POST['phone']
          email=request.POST['mail']
          desi=request.POST['des']
          uname=request.POST['uname']
          passw=request.POST['pswd']

          a=login(username=uname,password=passw,usertype='staff')
          a.save()

          b=staff(firstname=fname,lastname=lname,place=place,phone=phone,email=email,designation=desi,login=a)
          b.save()

          return HttpResponse("<script>alert('Registered');window.location='/viewstaff';</script>")
     return render(request,"staff.html")

def vstaff(request):
     data=staff.objects.all()
     return render(request,"viewstaff.html",{'a':data})

def delete(request,id):
     d=staff.objects.get(login_id=id)
    
     c=login.objects.get(login_id=id)

     d.delete()

     c.delete()

     return HttpResponse("<script>alert('Deleted');window.location='/viewstaff';</script>")

def stdreg(request):
    return render(request,"student.html")

def viewstudent(request):
    data=student.objects.all()
    return render(request,"viewstudent.html",{'b':data})

def mngcourse(request):
    data=course.objects.all()
    if request.method=='POST':
        cor=request.POST['course']
        a=course(course=cor)
        a.save()

    return render(request,"viewcourse.html",{'c':data})

def cordelete(request,id):
     d=course.objects.get(course_id=id)
     d.delete()

     return HttpResponse("<script>alert('Deleted');window.location='/managecourse';</script>")

def cup(request,id):
    x=course.objects.get(course_id=id)
    if request.method=='POST':
        cor=request.POST['course']
        x.course=cor
        x.save()
        return HttpResponse("<script>alert('updateed');window.location='/managecourse';</script>")
        

    return render(request,"courseupdate.html",{'c':x})


def mngsub(request):
    data=subject.objects.all()
    a=course.objects.all()
    if request.method=='POST':
        sub=request.POST['subject']
        cid=request.POST['course']

        b=subject(subject=sub,course_id=cid)
        b.save()
    return render(request,"viewsubject.html",{'d':data,'h':a})

def subdlt(request,id):
     d=subject.objects.get(subject_id=id)
     d.delete()

     return HttpResponse("<script>alert('Deleted');window.location='/managesubject';</script>")

def subupd(request,id):
    x=subject.objects.get(subject_id=id)
    if request.method=='POST':
        sub=request.POST['subject']
        x.subject=sub
        x.save()
        return HttpResponse("<script>alert('updateed');window.location='/managesubject';</script>")
        

    return render(request,"subjectupdate.html",{'d':x})

def viewfeed(request):
    data=feedback.objects.all()

    return render(request,"viewfeedback.html",{'e':data})

def viewlev(request):
    data=leave.objects.all()
    return render(request,"viewleave.html",{'f':data})

def accept(request,id):
    x=login.objects.get(login_id=id)

    x.usertype='student'
    x.save()
    return HttpResponse("<script>alert('Accepted');window.location='/viewstudent';</script>")

def reject(request,id):
    y=login.objects.get(login_id=id)
    
    y.usertype='rejected'
    y.save()
    return HttpResponse("<script>alert('Rejected');window.location='/viewstudent';</script>")

def stupdate(request,id):
    x=staff.objects.get(login_id=id)
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        place=request.POST['place']
        phone=request.POST['phone']
        mail=request.POST['mail']
        des=request.POST['des']
        x.firstname=fname
        x.lastname=lname
        x.place=place
        x.phone=phone
        x.email=mail
        x.designation=des
        x.save()
        return HttpResponse("<script>alert('updateed');window.location='/viewstaff';</script>")
        

    return render(request,"staffupdate.html",{'x':x})

# def sndrply(request,id):
#     x=feedback.objects.get(user_id=id)
#     if request.method=='POST':
#         rply=request.POST['reply']
#         x.reply=rply
#         x.save()
#         return HttpResponse("<script>alert('success');window.location='/viewfeedback';</script>")
    
#     return render(request,"sendreply.html",{'x':x})

def viewparent(request,id):
    data=parent.objects.filter(login_id=id)
    return render(request, "viewparent.html", {'g': data})

def viewatt(request,id):
    x=attendance.objects.filter(student_id=id)
    return render(request, "viewattendance.html", {'h': x})

def vsstd(request):
    data=student.objects.all()
    return render(request,"viewstudent(staff).html",{'i':data})

def vastaff(request,id):
    x=attendance.objects.filter(student_id=id)
    if request.method=='POST':
        attt=request.POST['aattendance']
        aadate=request.POST['adate']
        h=attendance(attendance=attt,date=aadate,student_id=id)
        h.save()

    return render(request, "viewattendance(staff).html",{'jj':x})

def attupd(request,id):
    x=attendance.objects.get(attendance_id=id)
    if request.method=='POST':
        att=request.POST['attendance']
        adate=request.POST['date']
        x.attendance=att
        x.date=adate
        x.save()
        return HttpResponse("<script>alert('updateed');window.location='/viewstudent(staff)';</script>")
        

    return render(request,"updateattendance.html",{'j':x})

def rslt(request,id):
    data=result.objects.all()
    a=subject.objects.all()
    if request.method=='POST':
        mrk=request.POST['marks']
        sid=request.POST['subject']

        b=result(marks=mrk,subject_id=sid,student_id=id)
        b.save()
        return HttpResponse("<script>alert('Added');window.location='/viewstudent(staff)'</script>")
    return render(request,"result.html",{'l':data,'k':a})

def sndntc(request,id):
    if request.method=='POST':
        nots=request.POST['ntc']
        c=notice(notice=nots,student_id=id)
        c.save()
        return HttpResponse("<script>alert('Sent');window.location='/viewstudent(staff)'</script>")
    return render(request,"sendnotice.html")
    
def aplylev(request):
    

    if request.method=='POST':
        date=request.POST['ldate']
        try:

            l=staff.objects.get(login_id=request.session['lid'])
            if l:
                d=leave(date=date,status='pending',send_id=request.session['lid'],sendby=l.firstname)
                d.save()
            else:
                d=leave(date=date,status='pending',send_id=request.session['lid'],sendby='no name')
                d.save()

                
        except:
            try:

                    s=student.objects.get(login_id=request.session['lid'])
                
                    if s:

                        d=leave(date=date,status='pending',send_id=request.session['lid'],sendby=s.fname)
                        d.save()

            except:
                    d=leave(date=date,status='pending',send_id=request.session['lid'],sendby='no name')
                    d.save()
            
    return render(request,"applyleave.html")

from datetime import *

def stafffeed(request):
    if request.method=='POST':
        feedbac=request.POST['feed']
       
        f=feedback(feedback=feedbac,reply='pending',date=datetime.now().date(),user_id=request.session['lid'])
        f.save()
        
    return render(request,"sendfeedback(staff).html")

def viewcrs(request):
    data=course.objects.all()
    return render (request,"viewcourse(student).html",{'m':data})

def viewsub(request,id):
    data=subject.objects.filter(course_id=id)
    return render(request,"viewsubject(student).html",{'n':data})

def stdatt(request):
    data=attendance.objects.filter(student_id=request.session['sid'])
    return render(request,"viewattendance(student).html",{'o':data})

def viewrslt(request):
    data=result.objects.filter(student_id=request.session['sid'])
    return render(request,"viewresult.html",{'p':data})     

def applylev(request):
    

    if request.method=='POST':
        date=request.POST['ldate']
        try:

            l=staff.objects.get(login_id=request.session['lid'])
            if l:
                d=leave(date=date,status='pending',send_id=request.session['lid'],sendby=l.firstname)
                d.save()
            else:
                d=leave(date=date,status='pending',send_id=request.session['lid'],sendby='no name')
                d.save()

                
        except:
            try:

                    s=student.objects.get(login_id=request.session['lid'])
                
                    if s:

                        d=leave(date=date,status='pending',send_id=request.session['lid'],sendby=s.fname)
                        d.save()

            except:
                    d=leave(date=date,status='pending',send_id=request.session['lid'],sendby='no name')
                    d.save()
            
    return render(request,"applyleave(student).html")

def stdfeed(request):
    if request.method=='POST':
        fdbac=request.POST['stufeed']
       
        f=feedback(feedback=fdbac,reply='pending',date=datetime.now().date(),user_id=request.session['lid'])
        f.save()
        
    return render(request,"sendfeedback(student).html")

def parentreg(request):
     if request.method=='POST':
          fnamep=request.POST['pfname']
          lnamep=request.POST['plname']
          placep=request.POST['pplace']
          phonep=request.POST['pphone']
          emailp=request.POST['pmail']
          uname=request.POST['uname']
          passw=request.POST['pswd']

          a=login(username=uname,password=passw,usertype='parent')
          a.save()

          b=parent(fname=fnamep,lname=lnamep,place=placep,phone=phonep,email=emailp,login=a)
          b.save()

          return HttpResponse("<script>alert('Registered');window.location='/login';</script>")
     return render(request,"parent.html")

def stdreg(request):
     data=student.objects.filter(parent_id=request.session['pid'])
     d=course.objects.all()
     if request.method=='POST':
          fname=request.POST['sfname']
          lname=request.POST['slname']
          place=request.POST['splace']
          phone=request.POST['sphone']
          email=request.POST['smail']
          cor=request.POST['course']
          uname=request.POST['uname']
          passw=request.POST['pswd']

          a=login(username=uname,password=passw,usertype='student')
          a.save()

          b=student(fname=fname,lname=lname,place=place,phone=phone,email=email,course_id=cor,login=a,parent_id=request.session['pid'])
          b.save()

          return HttpResponse("<script>alert('Registered');window.location='/student';</script>")
     return render(request,"student.html",{'q':d, 's':data})

def prntatt(request,id):
    data=attendance.objects.filter(student_id=id)
    return render(request,"viewattendance(parent).html",{'t':data})

def prntrslt(request,id):
    data=result.objects.filter(student_id=id)
    return render(request,"viewresult(parent).html",{'u':data})

def pntc(request):
    z=student.objects.get(parent_id=request.session['pid'])
    data=notice.objects.filter(student_id=z.student_id)
    return render(request,"viewnotice.html",{'v':data})

def pfeed(request):
    if request.method=='POST':
        pfdbac=request.POST['parfeed']
       
        f=feedback(feedback=pfdbac,reply='pending',date=datetime.now().date(),user_id=request.session['lid'])
        f.save()
        
    return render(request,"sendfeedback(parent).html")

def upldimg(request):
    data=sandeep.objects.all()
    if request.method=='POST':
        img=request.FILES['file']
        fs=FileSystemStorage()
        photo=fs.save(img.name,img)
        p=sandeep(img_name=photo)
        p.save()
        

    return render(request,"image.html",{'w':data})

