from django.shortcuts import render
from testapp.forms import Tourist,Guide,Language_Form
from testapp.models import User,language_Selection
from testapp.models import Tourist_Registration,Guide_Registration,Guide_Booking_Model
from django.contrib.auth.hashers import make_password
# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
import smtplib
import csv
import email
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Create your views here.
def Hyderabad_view1(request):
    return render(request,'testapp/hyderabad/hyderabad1.html')
def Warangal_view1(request):
    return render(request,'testapp/warangal/warangal.html')
def Vijayawada_view1(request):
    return render(request,'testapp/vijaywada/vijayawada1.html')
def Vizag_view1(request):
    return render(request,'testapp/vizag/vizag.html')
def Adilabad_view1(request):
    return render(request,'testapp/adilabad/adilabad1.html')
def Hyderabad_view2(request):
    return render(request,'testapp/hyderabad/hyderabad2.html')
def Warangal_view2(request):
    return render(request,'testapp/warangal/warangal2.html')
def Vijayawada_view2(request):
    return render(request,'testapp/vijaywada/vijayawada2.html')
def Vizag_view2(request):
    return render(request,'testapp/vizag/vizag2.html')
def Adilabad_view2(request):
    return render(request,'testapp/adilabad/adilabad2.html')
def Hyderabad_view3(request):
    return render(request,'testapp/hyderabad/hyderabad3.html')
def Warangal_view3(request):
    return render(request,'testapp/warangal/warangal3.html')
def Vijayawada_view3(request):
    return render(request,'testapp/vijaywada/vijayawada3.html')
def Vizag_view3(request):
    return render(request,'testapp/vizag/vizag3.html')

def index(request):

    return render(request,'testapp/index.html')

def tourist_index(request):
    return render(request,'testapp/tourist_details.html')

def special(request) :
    return HttpResponse("you are logged in,Nice!")

def tourist_logout(request):
    logout(request)
    return render(request,'testapp/index.html')

def guide_logout(request):
    logout(request)
    return render(request,'testapp/index.html')
def Tourist_registration(request):
    registered=False
    if request.method=="POST":
            first_name = request.POST.get('Firstname')
            print(first_name)
            last_name=request.POST.get('Lastname')
            user_name=request.POST.get('Username')
            email_id=request.POST.get('Email')
            pass_word = request.POST.get('Password')
            language=request.POST.get('language')
            gender=request.POST.get('gender')
            age=request.POST.get('age')
            phone_number=request.POST.get('Phonenumber')
            enc_password=make_password(pass_word)
            user=User(username=user_name,password=enc_password)
            user.is_tourist=True
            user.is_guide=False
            user.email=email_id
            try:
                user.save()
                form=Tourist_Registration(first_name=first_name,last_name=last_name,user_name=user_name,email_id=email_id,pass_word=pass_word,language=language,gender=gender,age=age,phone_number=phone_number)
                t=form.save()
            except:
                messages.warning(request, 'username or Email already exists Please Try again with New one')
                return HttpResponseRedirect('testapp/index.html')

            registered = True
            messages.success(request, 'successfully Registered Please Login!')
            return HttpResponseRedirect('testapp/index.html')
    else:
        return render(request,'testapp/index.html')

def Guide_registration(request):
    registered=False
    if request.method=="POST":

        first_name = request.POST.get('Firstname')
        print(first_name)
        last_name = request.POST.get('Lastname')
        user_name = request.POST.get('Username')
        email_id = request.POST.get('Email')
        pass_word = request.POST.get('Password')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        phone_number = request.POST.get('Phonenumber')
        native_place=request.POST.get('place')
        Address=request.POST.get('address')
        enc_password = make_password(pass_word)
        user = User(username=user_name, password=enc_password)
        user.is_tourist = False
        user.is_guide = True
        user.email=email_id
        try:
            user.save()
            form=Guide_Registration(first_name=first_name,last_name=last_name,user_name=user_name,email_id=email_id,pass_word=pass_word,gender=gender,age=age,phone_number=phone_number,native_place=native_place,Address=Address)
            t=form.save()

        except:
                messages.warning(request,'username or Email already exists Please Try again with new')
                return HttpResponseRedirect("testapp/index.html")
        registered = True
        messages.success(request, 'successfully Registered Please Login to Select the Languages you Known!')
        return HttpResponseRedirect("testapp/index.html")

    else:
       return render(request,'testapp/index.html')



def tourist_login(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user and user.is_tourist==True:
            if user.is_active:
                login(request,user)
                return render(request,"testapp/tourist_details.html",{'user':user})
            else:
                return render(request,'testapp/index.html')

        else:
            messages.warning(request, 'Invalid credentials!')
            return  HttpResponseRedirect("testapp/index.html")

    else:
        return render(request,'testapp/index.html',{})


def guide_login(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password,is_guide=True,is_tourist=False)
        if user and user.is_guide==True:
            if user.is_active:
                login(request,user)
                return render(request,"testapp/guide_details.html",{'user':user})
            else:
                return render(request,"testapp/index.html")

        else:
            messages.warning(request,'Please Enter Correct details!')
            return HttpResponseRedirect("testapp/index.html")
    else:
        return render(request,'testapp/index.html',{})

def tourist_language_view(request):
    if request.method=='POST':
        #guide_obj=User.objects.get(username=request.user)
        guide_obj = Guide_Registration.objects.get(user_name=request.user)
        #print(guide_obj)
        try:
              check= language_Selection.objects.get(user=guide_obj)
        except:
            check=None
        if check is None:
            ob1=language_Selection(user=guide_obj,languages_select=request.POST.getlist('languages_select'))
            #print(guide_obj,ob1.languages_select)
            #print(request.POST.getlist('languages_select'))
            ob1.save()
        else:
            list_of_lang=check.languages_select
            check.languages_select=request.POST.getlist('languages_select')
            #selection=form.cleaned_data.get('languages_select')
            check.save()
        return render(request,'testapp/guide_details.html')
    else:
        return render(request,'testapp/language_add.html')

def guide_booking_view(request):
    if request.method =='POST':
        date_value=(request.POST.get('date'))
        place_value=request.POST.get('place')
        gender_value = request.POST.get('gender')
        user_value=request.user
        language_value=request.POST.get('language')
        print(date_value,place_value,gender_value,language_value)
        try:
            guide_obj=Guide_Registration.objects.exclude(guide_booking_model__date_field=date_value).filter(native_place=place_value,gender=gender_value)
            query_set_list=[]
            print(guide_obj)
            for query_obj in guide_obj:
                try:
                   p=language_Selection.objects.get(user=query_obj.id)
                   checking=language_value in p.languages_select
                   if(checking==True):
                        query_set_list.append(query_obj)
                except:
                    pass
            print(query_set_list)
            return render(request,'testapp/display_available.html',{'query_set_list':query_set_list,'date_value':date_value})
        except:

            return render(request, 'testapp/display_available.html', {'query_set_list': query_set_list,'date_value':date_value})

    else:
        return render(request,'testapp/guide_book.html')


def display_book_view(request):
    print(request.user)
    guideid = request.GET['id']
    tourist_name=(request.GET['id1'])
    tourist_obj=Tourist_Registration.objects.get(user_name=tourist_name)
    date_value=request.GET['date_value']
    guide_obj=Guide_Registration.objects.get(id=guideid)
    print(guide_obj)
    print(tourist_obj)
    book_obj = Guide_Booking_Model(tourist_username=tourist_obj, guide_username=guide_obj, date_field=date_value)
    book_obj.save()
    print("YOU SuccessFully Booked a Guide")
    return mail_send(request,tourist_obj.id,guide_obj.id,date_value)

def mail_send(request,tourist_id,guide_id,date_value):
    fromaddr = "miniproject.vce2019@gmail.com"
    tourist_obj=Tourist_Registration.objects.get(id=tourist_id)
    guide_obj=Guide_Registration.objects.get(id=guide_id)
    tourist_email=tourist_obj.email_id
    guide_email=guide_obj.email_id
    toaddr = tourist_email
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Guide details from TravelGuide Website"

    body = "your are successfully booked a guide!   "+"    Details of guide you booked are phone number: "+guide_obj.phone_number+"  Guide Address: "+guide_obj.Address+"  Guide Email Address: "+guide_obj.email_id+"    Please contact him if you have any queries"

    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "MiniProject2019")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)

    server.quit()
    toaddr = guide_email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Tourist details from TravelGuide Website"

    body = "your have a Booking on "+date_value+ "   Tourist Phone Number: " + tourist_obj.phone_number + "    Tourist Email Address: " + tourist_obj.email_id + "  Please contact him if you have any queries"

    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "MiniProject2019")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    return render(request,'testapp/tourist_details.html')