from django.shortcuts import render
from .models import place_details,user_details,new_table
from django.contrib import messages
from django.core.mail import send_mail
from django.db import connection
import pandas as pd
from django.conf import settings


cur = connection.cursor()



# Create your views here.

def index(request):
    return render(request,'index.html')

def abc(request):
    return render(request,'admin.html')

def addd(request):
    if request.method == 'POST':
        data = place_details()
        data.place = request.POST['Place']
        data.number_of_beds = request.POST['number_of_beds']
        print(data.place)
        print(data.number_of_beds)
        data.save()
        messages.success(request,'Place and Beds Count added Successfuly')
        return render(request, 'admin.html')
    return render(request, 'admin.html')


def display(request):
    data=place_details.objects.all()
    print(data)
    return render(request,'informa.html',{'data':data})

def users(request):
    return render(request,'users.html')

def search(request):
    if request.method=='POST':
        Place=request.POST['Place']
        status=place_details.objects.filter(place=Place)
        return render(request, 'display.html', {"data": status})
    return render(request, 'search.html')


def disp(request):
    data = place_details.objects.all()
    print(data)
    return render(request,'disp.html',{'data':data})

def mmi(request):
    return render(request,'mmi.html')


# user system information
def Symptoms(request):
    global Email
    if request.method=='POST':
        print('---------------')
        sql="select Email from firstapp_user_details"
        cur.execute(sql)
        data=cur.fetchall()
        connection.commit()
        d=user_details()
        d.Name=request.POST['Name']
        d.Age=request.POST['Age']
        d.Email=request.POST['Email']
        d.Gender=request.POST['Gender']
        d.Contact=request.POST['Contact']
        d.Hometown=request.POST['Hometown']
        d.symptom1=request.POST['symptom1']
        d.symptom2 = request.POST['symptom2']
        d.symptom3=request.POST['symptom3']
        d.symptom4 = request.POST['symptom4']
        print(d.symptom1)
        print(d.symptom2)
        print(d.symptom3)
        print(d.symptom4)
        for i in data:
            print(i)
            if d.Email in i:
                print("Hello")
                messages.success(request, "Email already exist")
                return render(request, 'mmi.html')
        d.save()
        messages.success(request,"Details added Successfully")
        return render(request,'mmi.html')

# user medical information
def medic_info(request):
    data=user_details.objects.all()
    print(data)
    return render(request,"medicinfo.html",{'data':data})

def ssss(request,id,Email,Name,Age,Gender,Contact,Hometown,symptom1,symptom2,symptom3,symptom4):
    sql="select EMail from firstapp_new_table"
    cur.execute(sql)
    data=cur.fetchall()
    connection.commit()
    print(data)
    for i in data:
        print(i[0])
        if Email in i[0]:
            messages.success(request, "Email already existing")
            return render(request, "update.html")

    request.session['Name']=Name
    sql="insert into firstapp_new_table(Name,Age,Email,Gender,Contact,Hometown,symptom1,symptom2,symptom3,symptom4) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(Email,Age,Name,Gender,Contact,Hometown,symptom1,symptom2,symptom3,symptom4)
    cur.execute(sql,val)
    connection.commit()
    x=request.session['Name']
    sql="update firstapp_place_details set Email='%s' where Email='null' "%(x)
    cur.execute(sql)
    connection.commit()
    messages.success(request, "Request sent Successfully to ADMIN")
    return render(request,"update.html")



def allrequest(request):
    print(request.session['Name'])
    data = new_table.objects.all()

    return render(request,'allrequest.html',{'data':data})



def uvw(request,place,number_of_beds):
    sql="update firstapp_new_table set place='%s',number_of_beds='%s' where place='none' and number_of_beds='none' " %(place,number_of_beds)
    cur.execute(sql)
    connection.commit()
    messages.success(request, "data updated successfully")
    return render(request,'to.html')



def ms(request,Hometown,Email,Name):
    subject = 'Qurentine Bed Booking'
    message = f'Hi {Name}'
    content='Your Bed is Booked successfully.'
    m1="This message is automatic generated so dont reply to this Mail"
    m2="Thanking you"
    m3="Regards"
    m4="ADMIN."
    print(message)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [Email]
    print(recipient_list)
    text=message + '\n' + content + '\n' + m1  + '\n' + m2 + '\n' + m3 + '\n' + m4
    send_mail(subject, text, email_from, recipient_list,fail_silently=False,)
    sql="select * from firstapp_place_details where place='%s'"%(Hometown)
    cur.execute(sql)
    data=cur.fetchall()
    connection.commit()
    print(data)
    n=1
    for i in data:
        m=int(i[2])
        z=(m-n)
        print(z)
        sql="update firstapp_place_details set number_of_beds='%s' where place='%s'"%(z,Hometown)
        cur.execute(sql)
        connection.commit()
        messages.success(request, "Mail Sent successfully")
        return render(request, 'ms.html')
    return render(request, 'ms.html')


