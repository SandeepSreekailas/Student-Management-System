from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
    path("",views.home),
    path("login",views.logins),
    path("adminhome",views.adhome),
    path("staffhome",views.sthome),
    path("staff",views.staffreg),
    path("viewstaff",views.vstaff),
    path("cordelete/<id>",views.cordelete),
    path("stupdate/<id>",views.stupdate),
    path("delete/<id>",views.delete),
    path("studenthome",views.stuhome),
    path("student",views.stdreg),
    path("viewstudent",views.viewstudent),
    path("viewparent/<id>",views.viewparent),
    path("viewattendance/<id>",views.viewatt),
    path("accept/<id>",views.accept),
    path("reject/<id>",views.reject),
    path("managecourse",views.mngcourse),
    path("corupdate/<id>",views.cup),
    path("managesubject",views.mngsub),
    path("subdelete/<id>",views.subdlt),
    path("subupadate/<id>",views.subupd),
    path("viewfeedback",views.viewfeed),
    # path("sendrply/<id>",views.sndrply),
    path("viewleave",views.viewlev),

    path("viewstudent(staff)",views.vsstd),
    path("viewattend/<id>",views.vastaff),
    path("attupdate/<id>",views.attupd),
    path("result/<id>",views.rslt),
    path("sendnotice/<id>",views.sndntc),
    path("sendfeedback",views.stafffeed),
    path("applyleave",views.aplylev),
    path("uploadimage",views.upldimg),

    path("viewcourse",views.viewcrs),
    path("viewsubject/<id>",views.viewsub),
    path("viewattendance1",views.stdatt),
    path("viewresult",views.viewrslt),
    path("applyforleave",views.applylev),
    path("sendfeedbackstd",views.stdfeed),

    path("parent",views.parentreg),
    path("parenthome",views.prnthome),
    path("viewattendancep/<id>",views.prntatt),
    path("viewresultp/<id>",views.prntrslt),
    path("viewnotice",views.pntc),
    path("viewfeedbackp",views.pfeed),
]