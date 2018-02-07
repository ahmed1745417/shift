from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.db import connection
from django.conf import settings


import cgi,cgitb,datetime


from .models import Emp

from .forms import DateForm

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'shiftroster/index.html'
    context_object_name = 'emp_list'

    
    
    def get_queryset(self):
        date=datetime.date.today()
        if date.month == 12:
            last_day=date.replace(day=31)
        else:
            last_day= date.replace(month=date.month+1, day=1) - datetime.timedelta(days=1)
        
    
        
        first_day =date.replace(month=date.month, day=1)
        cursor=connection.cursor()
        today=datetime.date.today()
        cursor.execute("select shift_date,shift,name from shiftroster_roster where shift_date>='%s' and shift_date<='%s'and shift!='Week Off' and shift!='Leave' order by shift_date,field(shift,'Morning Shift','Afternoon Shift','Night Shift'),name" % (first_day,last_day))
        data=cursor.fetchall()
#a=[]
#a.append([])
#a.append([])
#a[0].append(data[0])
#a[0].append(data[0])
#a[1].append(data[0])
#a[1].append(data[0])

#print(a[0][1])
        j=0
        z=4
        x=0
        y=0
        data1=[]
        #data1.append([])
        j=0
        if data :
            data1.append([])
            data1[j].append(data[0][0])
	#data1[j].append(data[0][0])
        for emp in data:
            if(emp[1]=='Morning Shift'):
                
                
                if(z<3):
                    for i in range(z,3):
                        data1[j].append("-")
                        z=z+1
                    z=4
                    data1.append([])
                    j=j+1
                    data1[j].append(emp[0])
                elif(z==3):
                    data1.append([])
                    j=j+1
                    data1[j].append(emp[0])
                    z=4
                        
                    
                data1[j].append(emp[2])
                x=x+1
                y=0
                continue
    

            
            elif(emp[1]=='Afternoon Shift'):
                if(x<3):
                    for i in range(x,3):
                        data1[j].append("-")
                        x=x+1
                
                data1[j].append(emp[2])
                y=y+1
                z=0
                continue

            
            elif(emp[1]=='Night Shift'):
                if(y<3):
                    for i in range(y,3):
                        data1[j].append("-")
                        y=y+1
                
                data1[j].append(emp[2])
                z=z+1
                x=0
                continue
        if(z<3):
            for i in range(z,3):
                data1[j].append("-")
 #   cursor.callproc("shift_roster",(startdate,enddate))
#      cursor.execute("select shift_date,shift,name from shiftroster_roster where shift_date='2016-7-1' and shift!='Week Off' order by shift_date,field(shift,'Morning Shift','Afternoon Shift','Night Shift'),name")
#        data=cursor.fetchall()
 #       i=0
 #       select 
 #       for emp1 in data:
 #           j=0
 #           for emp2 in emp1:
 #               data1[i][j]=emp2[j]
 #               j=j+1
 #           i=i+1
            
        return data1
    
def calculate(request):
    template_name = loader.get_template('shiftroster/results.html')
   
    startdate=request.POST['startdate']
    enddate=request.POST['enddate']
    sa_startdate=request.POST['sa_startdate']
    sa_enddate=request.POST['sa_enddate']
    ta_startdate=request.POST['ta_startdate']
    ta_enddate=request.POST['ta_enddate']
    cursor=connection.cursor()
#   cursor.callproc("shift_roster",(startdate,enddate))
    cursor.execute("select shift_date,shift,name from shiftroster_roster where shift_date>='%s' and shift_date<='%s'and shift!='Week Off' and shift!='Leave' order by shift_date,field(shift,'Morning Shift','Afternoon Shift','Night Shift'),name" % (startdate,enddate))
    data=cursor.fetchall()
    j=0
    z=4
    x=0
    y=0
    vdata=[]

    j=0
    if data:
        
        vdata.append([])
        vdata[j].append(data[0][0])
    for emp in data:
        if(emp[1]=='Morning Shift'):
                
                
            if(z<3):
                for i in range(z,3):
                    vdata[j].append("-")
                    z=z+1
                z=4
                vdata.append([])
                j=j+1
                vdata[j].append(emp[0])
            elif(z==3):
                vdata.append([])
                j=j+1
                vdata[j].append(emp[0])
                z=4
                        
                    
            vdata[j].append(emp[2])
            x=x+1
            y=0
            continue
    

            
        elif(emp[1]=='Afternoon Shift'):
            if(x<3):
                for i in range(x,3):
                    vdata[j].append("-")
                    x=x+1
                
            vdata[j].append(emp[2])
            y=y+1
            z=0
            continue

            
        elif(emp[1]=='Night Shift'):
            if(y<3):
                for i in range(y,3):
                    vdata[j].append("-")
                    y=y+1
                
            vdata[j].append(emp[2])
            z=z+1
            x=0
            continue
    if(z<3):
        for i in range(z,3):
            vdata[j].append("-")

    cursor.execute("select eid,name,sum(if (shift='Morning Shift',1,0)) as Morning,sum(if (shift='Afternoon Shift',1,0)) as Afternoon,sum(if (shift='Night Shift',1,0)) as Night,sum(if (shift='Night Shift',200,if (shift='Afternoon Shift',200,if (shift='Morning Shift',150,0)))) as total from shiftroster_roster where eid in (select distinct eid from shiftroster_emp) and (shift_date>= '%s' and shift_date<='%s') group by eid" % (sa_startdate,sa_enddate))
    sa_data=cursor.fetchall()

    cursor.execute("select eid,name,sum(if (shift='Morning Shift',1,0)) as Morning,sum(if (shift='Afternoon Shift',1,0)) as Afternoon,sum(if (shift='Night Shift',1,0)) as Night,sum(if (shift='Night Shift',400,if (shift='Afternoon Shift',200,if (shift='Morning Shift',200,0)))) as total from shiftroster_roster where eid in (select distinct eid from shiftroster_emp) and (shift_date>= '%s' and shift_date<='%s') group by eid" % (ta_startdate,ta_enddate))
    ta_data=cursor.fetchall()
#    emp_list=vdata
#    context={'emp_list':emp_list,'vdata':vdata,'sa_data':sa_data,'ta_data':ta_data}
    context={'vdata':vdata,'sa_data':sa_data,'ta_data':ta_data}
    return HttpResponse(template_name.render(context,request))


def exchange(request):
    template_name = loader.get_template('shiftroster/results.html')
   
    exsourcename=request.POST['exsourcename']
    exdestname=request.POST['exdestname']
    exsourcedate=request.POST['exsourcedate']
    exdestdate=request.POST['exdestdate']
    cursor=connection.cursor()
    cursor.execute("select shift,eid from shiftroster_roster where shift_date='%s' and name='%s'" %(exsourcedate,exsourcename))
    exsourcedata=cursor.fetchall()
    exsourceshift=exsourcedata[0][0]
    exsourceid=exsourcedata[0][1]
    cursor.execute("select shift,eid from shiftroster_roster where shift_date='%s' and name='%s'" %(exdestdate,exdestname,))
    exdestdata=cursor.fetchall()
    exdestshift=exdestdata[0][0]
    exdestid=exdestdata[0][1]

    cursor.execute("update shiftroster_roster set shift_date='%s',name='%s',eid='%s',shift='%s' where shift_date='%s' and name='%s' and shift='%s'"%(exdestdate,exsourcename,exsourceid,exdestshift,exdestdate,exdestname,exdestshift))
    cursor.execute("update shiftroster_roster set shift_date='%s',name='%s',eid='%s',shift='%s' where shift_date='%s' and name='%s' and shift='%s'"%(exsourcedate,exdestname,exdestid,exsourceshift,exsourcedate,exsourcename,exsourceshift))
    cursor.execute("select shift_date,shift,name from shiftroster_roster where shift_date='%s' or shift_date='%s'and shift!='Week Off' and shift!='Leave' order by shift_date,field(shift,'Morning Shift','Afternoon Shift','Night Shift'),name" % (exsourcedate,exdestdate))
    data=cursor.fetchall()
    j=0
    z=4
    x=0
    y=0
    vdata=[]

    j=0
    if data:
        
        vdata.append([])
        vdata[j].append(data[0][0])
    for emp in data:
        if(emp[1]=='Morning Shift'):
                
                
            if(z<3):
                for i in range(z,3):
                    vdata[j].append("-")
                    z=z+1
                z=4
                vdata.append([])
                j=j+1
                vdata[j].append(emp[0])
            elif(z==3):
                vdata.append([])
                j=j+1
                vdata[j].append(emp[0])
                z=4
                        
                    
            vdata[j].append(emp[2])
            x=x+1
            y=0
            continue
    

            
        elif(emp[1]=='Afternoon Shift'):
            if(x<3):
                for i in range(x,3):
                    vdata[j].append("-")
                    x=x+1
                
            vdata[j].append(emp[2])
            y=y+1
            z=0
            continue

            
        elif(emp[1]=='Night Shift'):
            if(y<3):
                for i in range(y,3):
                    vdata[j].append("-")
                    y=y+1
                
            vdata[j].append(emp[2])
            z=z+1
            x=0
            continue
    if(z<3):
        for i in range(z,3):
            vdata[j].append("-")
    i=5
    context={'i':i,'vdata':vdata}
    return HttpResponse(template_name.render(context,request))

def leave(request):
    template_name = loader.get_template('shiftroster/results.html')
   
    leavedate=request.POST['leavedate']
    leavename=request.POST['leavename']
    cursor=connection.cursor()
    cursor.execute("update shiftroster_roster set shift='Leave' where name='%s' and shift_date='%s'"%(leavename,leavedate))
    cursor.execute("select shift_date,shift,name from shiftroster_roster where shift_date='%s' and shift!='Week Off' and shift!='Leave' order by shift_date,field(shift,'Morning Shift','Afternoon Shift','Night Shift'),name" % (leavedate))
    data=cursor.fetchall()
    j=0
    z=4
    x=0
    y=0
    vdata=[]

    j=0
    if data:
        
        vdata.append([])
        vdata[j].append(data[0][0])
    for emp in data:
        if(emp[1]=='Morning Shift'):
                
                
            if(z<3):
                for i in range(z,3):
                    vdata[j].append("-")
                    z=z+1
                z=4
                vdata.append([])
                j=j+1
                vdata[j].append(emp[0])
            elif(z==3):
                vdata.append([])
                j=j+1
                vdata[j].append(emp[0])
                z=4
                        
                    
            vdata[j].append(emp[2])
            x=x+1
            y=0
            continue
    

            
        elif(emp[1]=='Afternoon Shift'):
            if(x<3):
                for i in range(x,3):
                    vdata[j].append("-")
                    x=x+1
                
            vdata[j].append(emp[2])
            y=y+1
            z=0
            continue

            
        elif(emp[1]=='Night Shift'):
            if(y<3):
                for i in range(y,3):
                    vdata[j].append("-")
                    y=y+1
                
            vdata[j].append(emp[2])
            z=z+1
            x=0
            continue
    if(z<3):
        for i in range(z,3):
            vdata[j].append("-")
    
    context={'vdata':vdata}
    return HttpResponse(template_name.render(context,request))
    
    
def test(request):
    template_name = loader.get_template('shiftroster/wfhtcr.htm')
    udaExec = teradata.UdaExec ()
    session = udaExec.connect("${dataSourceName}")
 
    #with udaExec.connect("${dataSourceName}") as session: 
    data=session.execute("select * from trm.employee_detail where e_empid=10316 or e_empid=10317")
    context={'data':data,'STATIC_URL': settings.STATIC_URL}
    return HttpResponse(template_name.render(context,request))

def generate(request):
    template_name = loader.get_template('shiftroster/results.html')
   
    genstartdate=request.POST['genstartdate']
    genenddate=request.POST['genenddate']
    cursor=connection.cursor()
    cursor.callproc("shift_roster",(genstartdate,genenddate))
    cursor.execute("select shift_date,shift,name from shiftroster_roster where shift_date>='%s' and shift_date<='%s'and shift!='Week Off' and shift!='Leave' order by shift_date,field(shift,'Morning Shift','Afternoon Shift','Night Shift'),name" %(genstartdate,genenddate))
    data=cursor.fetchall()
    j=0
    z=4
    x=0
    y=0
    vdata=[]

    j=0
    if data:
        
        vdata.append([])
        vdata[j].append(data[0][0])
    for emp in data:
        if(emp[1]=='Morning Shift'):
                
                
            if(z<3):
                for i in range(z,3):
                    vdata[j].append("-")
                    z=z+1
                z=4
                vdata.append([])
                j=j+1
                vdata[j].append(emp[0])
            elif(z==3):
                vdata.append([])
                j=j+1
                vdata[j].append(emp[0])
                z=4
                        
                    
            vdata[j].append(emp[2])
            x=x+1
            y=0
            continue
    

            
        elif(emp[1]=='Afternoon Shift'):
            if(x<3):
                for i in range(x,3):
                    vdata[j].append("-")
                    x=x+1
                
            vdata[j].append(emp[2])
            y=y+1
            z=0
            continue

            
        elif(emp[1]=='Night Shift'):
            if(y<3):
                for i in range(y,3):
                    vdata[j].append("-")
                    y=y+1
                
            vdata[j].append(emp[2])
            z=z+1
            x=0
            continue
    if(z<3):
        for i in range(z,3):
            vdata[j].append("-")
    
    context={'vdata':vdata}
    return HttpResponse(template_name.render(context,request))






def home(req):
    return render(req, 'shiftroster/main.html', {'STATIC_URL': settings.STATIC_URL})


class ResultsView(generic.ListView):
    template_name = 'shiftroster/results.html'
    context_object_name = 'roster_list'
    def get_queryset(self):
        """Return the last five published questions."""
        return HttpResponse("Done")   
    
#class GenerateView(generic.DetailView):
#   cursor=connection.cursor()
#    cursor.callproc("shift_roster",('2016-7-1','2016-7-4'));
#    return HttpResponse("Done")
    
