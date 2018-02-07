import pymysql
import datetime


connection = pymysql.connect("localhost","cloud","lt230062","cloud" )


cursor=connection.cursor()
#   cursor.callproc("shift_roster",(startdate,enddate))
cursor.execute("select shift_date,shift,name from shiftroster_roster where shift_date<'2016-7-5' and shift!='Week Off' order by shift_date,field(shift,'Morning Shift','Afternoon Shift','Night Shift'),name")
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
z=3
x=0
y=0
data1=[]
data1.append([])

j=0
data1[j].append(data[0][0])
for emp in data:
    if(emp[1]=='Morning Shift'):
            if(z<3):
                for i in range(z,3):
                    data1[j].append("-")
                    z=z+1
                data1.append([])
                j=j+1
                data1[j].append(emp[0])
                
                    
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


                    
#    
#    data1.append([])
#    for i in range(5):
#        if(emp1[t]==None:
#           t=t-1
#           break
#        data1[j].append(emp1[t])
#        t=t+1
#    j=j+1
       
print(data1)            
