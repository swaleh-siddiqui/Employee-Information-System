from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
import smtplib
from django.core.mail import send_mail
from email.message import EmailMessage
import ssl


# Create your views here.

def index(request):
    return render(request,"index.html")

def register(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")

    eror = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['employeeid']
        em = request.POST['emailid']
        pwd = request.POST['createpassword']

        try:
        
            user = User.objects.create_user(first_name = fn,last_name = ln, username = ec, password = pwd, email=em)
            EmployeeSignup.objects.create(user = user , empcode = ec)

            # send_mail(
            #     "Employee Login Credentials",
            #     "Username - " + ec + "/n" + "Password - " + pwd + "/n You can Change the password once you log in .",
            #     "sufi590eis@gmail.com",
            #     [em]
            # )

            msg = EmailMessage()
            msg['From'] = 'sufiyaniffco@gmail.com'
            msg['To'] = em
            msg['Subject'] = "Employee Log in credentials"
            msg.set_content("Username - " + ec + "\n" + "Password - " + pwd + "\n You can Change the password once you log in .")
            
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            print("hhh")
            server.starttls()
            print("hhh")
            server.login("sufiyaniffco@gmail.com" , "rrsyfoujdzvucsie")
            print("hhh")
            server.sendmail("sufiyaniffco@gmail.com", em , msg.as_string())
            print("hhh")
            server.close()

            # ema = EmailMessage()
            # ema["From"] = "sufi590eis@gmail.com"
            # ema["To"] = em
            # ema["Subject"] = "Employee Log In credentials"
            # ema.set_content("Username - " + ec + "/n" + "Password - " + pwd + "/n You can Change the password once you log in .")  
            # with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp :
            #     smtp.login("sufi590eis@gmail.com", "hxyhotqksauzjwbi")
            #     smtp.sendmail("sufi590eis@gmail.com",em , ema.as_string())

            eror = "yes"
        except:
            eror = "no"

    return render(request,"register.html",locals())

def emp_login(request):
    eror = ""
    if request.method == "POST":
        u = request.POST['employeeid']
        p = request.POST['password']
        user = authenticate(username = u, password = p)
        if user:
            login(request,user)
            eror = "yes"
        else :
            eror = "no"
    return render(request,"emp_login.html",locals())



def emp_home(request):
    if not request.user.is_authenticated:
        return redirect("emp_login")
    user = request.user
    employee = EmployeeSignup.objects.get(user = user)
    return render(request,"emp_home.html", locals())

def profile(request):
    if not request.user.is_authenticated:
        return redirect("emp_login")
    user = request.user
    employee = EmployeeSignup.objects.get(user = user)
    return render(request,"profile.html", locals())

def Logout(request):
    logout(request)
    return redirect("index")

def emp_edit_profile(request):
    if not request.user.is_authenticated:
        return redirect("emp_emp_login")

    eror = ""
    user = request.user
    employee = EmployeeSignup.objects.get(user = user)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['emailid']
        dob = request.POST['dateofbirth']
        bg = request.POST['bloodgroup']
        g = request.POST['gender']
        adhar = request.POST['aadharno']
        pan = request.POST['panno']
        b_acc = request.POST['bankaccountno']
        ifsc = request.POST['ifsccode']
        fname = request.POST['fathername']
        mname = request.POST['mothername']
        mstat = request.POST['maritalstatus']
        cont = request.POST['contactno']
        ad = request.POST['address']
        dep = request.POST['department']
        des = request.POST['designation']
        image = request.FILES['profilepicture']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.user.email = em

        if dob:
            employee.dob = dob   
        if g:
            employee.gender = g
        if mstat:
            employee.status = mstat
        if bg:
            employee.blood_grp =  bg
        if image:
            employee.img = image


        employee.adhar = adhar
        employee.bank_acc = b_acc
        employee.pan = pan
        employee.ifsc_code = ifsc
        employee.address = ad
        
        
        employee.contact = cont
        employee.empdept = dep
        employee.designation = des
        
        employee.father_name = fname
        employee.mother_name = mname


        try:
            employee.save()
            employee.user.save()
            eror = "yes"
        except:
            eror = "no"

    return render(request,"emp_edit_profile.html",locals())


def emp_change_password(request):
    if not request.user.is_authenticated:
        return redirect("emp_login")
    eror = ""
    user = request.user
    employee = EmployeeSignup.objects.get(user = user)
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['createnewpassword']
        cn = request.POST['confirmnewpassword']

        try:
            if cn != n:
                return render(request,"emp_change_password.html",locals())
            if user.check_password(c):
                user.set_password(n)
                user.save()
                eror = "yes"
            else:
                eror = "not"
        except:
            eror = "no"

    return render(request,"emp_change_password.html",locals())


def admin_login(request):
    eror = ""
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username = u, password = p)
        try:
            if user.is_staff:
                login(request,user)
                eror = "yes"
            else :
                eror = "no"
        except:
            eror = "no"
    return render(request,"admin_login.html",locals())


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    return render(request,"admin_home.html")

def Logoutadmin(request):
    logout(request)
    return redirect("index")


def admin_change_password(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    eror = ""
    user = request.user

    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['createnewpassword']
        cn = request.POST['confirmnewpassword']

        try:
            if cn != n:
                return render(request,"admin_change_password.html",locals())
            if user.check_password(c):
                user.set_password(n)
                user.save()
                eror = "yes"
            else:
                eror = "not"
        except:
            eror = "no"

    return render(request,"admin_change_password.html",locals())


def admin_profile(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    
    eror = ""
    
    i = request.user
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['emailid']
        un = request.POST['username']

        if fn:
            request.user.first_name = fn 
        if ln:
            request.user.last_name = ln 
        if em:
            request.user.email = em 
        if un:
            request.user.username = un 

        try:
            i.save()
            eror = "yes"
        except:
            eror = "no"



    return render(request,"admin_profile.html",locals())



def admin_emp_details(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    
    emp = EmployeeSignup.objects.all()

    return render(request,"admin_emp_details.html", locals())


def delete_emp(request,id):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    
    user = User.objects.get(id = id)
    user.delete()

    return redirect("admin_emp_details")





def admin_edit_emp(request,id):
    if not request.user.is_authenticated:
        return redirect("admin_login")

    eror = ""
    user = User.objects.get(id = id)
    employee = EmployeeSignup.objects.get(user = user)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['emailid']
        dob = request.POST['dateofbirth']
        bg = request.POST['bloodgroup']
        g = request.POST['gender']
        adhar = request.POST['aadharno']
        pan = request.POST['panno']
        b_acc = request.POST['bankaccountno']
        ifsc = request.POST['ifsccode']
        fname = request.POST['fathername']
        mname = request.POST['mothername']
        mstat = request.POST['maritalstatus']
        cont = request.POST['contactno']
        ad = request.POST['address']
        dep = request.POST['department']
        des = request.POST['designation']
        image = request.FILES['profilepicture']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.user.email = em

        if dob:
            employee.dob = dob   
        if g:
            employee.gender = g
        if mstat:
            employee.status = mstat
        if bg:
            employee.blood_grp =  bg
        if image:
            employee.img = image


        employee.adhar = adhar
        employee.bank_acc = b_acc
        employee.pan = pan
        employee.ifsc_code = ifsc
        employee.address = ad
        
        
        employee.contact = cont
        employee.empdept = dep
        employee.designation = des
        
        employee.father_name = fname
        employee.mother_name = mname


        try:
            employee.save()
            employee.user.save()
            eror = "yes"
        except:
            eror = "no"

    return render(request,"admin_edit_emp.html",locals())




def admin_signup(request):
    eror = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        un = request.POST['username']
        em = request.POST['emailid']
        pwd = request.POST['createpassword']

        try:
            user = User.objects.create_user(first_name = fn,last_name = ln, username = un, password = pwd, email=em,is_staff = True,is_superuser = True)
            
            eror = "yes"
        except:
            eror = "no"
    return render(request,"admin_signup.html" , locals())





def alllogin(request):

    eror = ""
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username = u, password = p)
        try:
            if user.is_staff:
                login(request,user)
                eror = "ayes"
            elif user and user.is_staff == False:
                login(request,user)
                eror = "yes"
            else :
                eror = "no"
        except:
            eror = "no"

    return render(request,"login.html",locals())


