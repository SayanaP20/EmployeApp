from django.shortcuts import render

# Create your views here.
from ssl import CertificateError
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Employee

from .models import *




def index(request):
    return render(request,'index.html')


def  admin_view(request):
    return render(request,'view.html')   


# def user(request):
#     return render(request,'user.html')   


def admin_login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)  
        if user is not None:
            login(request,user)      
            return redirect('admin_view')
    else:
        return render(request,"admin.html",{'error_message':'invalid login credentials'})
    return render(request,'admin.html')




def insert_data(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        contact_number = request.POST['contact_number']
        dob = request.POST['dob']
        degree_name = request.POST['degree_name']
        institute_name= request.POST['institute_name']
        passing_year = request.POST['passing_year']
        percentage = request.POST['percentage']
        designation = request.POST['designation']
        department = request.POST['department']
        salary = request.POST['salary']
        certificate = request.FILES["certificate"]

        emp=Employee()
        emp.name=name
        emp.email=email
        emp.password=password
        emp.contact_number=contact_number
        emp.date_of_birth=dob
        emp.degree_name=degree_name
        emp.institute_name=institute_name
        emp. passing_year= passing_year
        emp.percentage=percentage
        emp.designation= designation
        emp.department=department
        # emp.salary=salary
        emp.salary = int(salary)
        emp.certificate=certificate
        emp.save()

        emp_id=emp.id
        Qual=Qualification()
        Qual.employee_id = emp_id
        Qual.degree_name=degree_name
        Qual.institute_name = institute_name
        Qual.passing_year = passing_year
        Qual.percentage = percentage
        Qual.save() 


        emp_id=emp.id
        exp = ExperienceCertificate()
        exp.employee_id = emp_id
        exp.certificate = request.FILES["certificate"]
        exp.save()
        
        return HttpResponse("data saved")
    else:
        return render(request, "admin.html") 



def add_employee(request):
    return render(request,"addemp.html")




def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST['password']
        print(email,password,"emaillllllllllllllll")
        try:
            user =Employee.objects.get(email=email, password=password)
            # login user
            request.session['user_id'] = user.id
            # redirect to the dashboard based on the user's department and designation
            if user.department == 'python':
                return redirect('python_dashboard', designation=user.designation)
            elif user.department == 'php':
                return redirect('php_dashboard', designation=user.designation)
            elif user.department == 'hr':
                return redirect('hr_dashboard', designation=user.designation)
        except Employee.DoesNotExist:
            return render(request, 'user.html', {'error': 'Invalid email or password'})
    else:
        return render(request, 'user.html')


def python_dashboard(request, designation):
    p= request.session['user_id']
    py=Employee.objects.get(id=p)
    desig=py.designation
    employees = Employee.objects.filter(department='python')
    return render(request, 'python_dashboard.html', {'employees': employees,"desig":desig})

def php_dashboard(request, designation):
    p= request.session['user_id']
    ph=Employee.objects.get(id=p)
    desig=ph.designation
    employees = Employee.objects.filter(department='php')
    return render(request, 'php_dashboard.html', {'employees': employees,"desig":desig})

def hr_dashboard(request, designation):
    employees = Employee.objects.filter(department='hr')
    return render(request, 'hr_dashboard.html', {'employees': employees})       




# hr section

def employee_list(request):
    employees = Employee.objects.all()
    departments = list(set([employee.department for employee in employees]))
    designations = list(set([employee.designation for employee in employees]))
    department = request.GET.get('department')
    designation = request.GET.get('designation')
    if department:
        employees = employees.filter(department=department)
    if designation:
        employees = employees.filter(designation=designation)
    return render(request, 'employee_list.html', {'employees': employees, 'departments': departments, 'designations': designations, 'selected_department': department, 'selected_designation': designation})







# add updates
def daily_updates(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        task = request.POST.get('task')
        eid= request.session['user_id']
        daily_update = DailyUpdate(date=date, task=task,employee_id=eid)
        daily_update.save() 
        return redirect("/daily_updates/")
    else:
        return render(request, 'daily_updates.html')


# view updates       
def view_updates(request):
    updates = DailyUpdate.objects.all()
    return render(request, 'view_updates.html', {'updates': updates})



# php employess

def php_view_juniors(request):
    data=Employee.objects.filter(department="php",designation="junior")
    return render(request,"php_view_juniors.html",{"data":data})

def php_view_seniors(request):
    data=Employee.objects.filter(department="php",designation="senior")
    return render(request,"php_view_juniors.html",{"data":data})


# python employees
def python_view_juniors(request):
    data=Employee.objects.filter(department="python",designation="junior")
    return render(request,"python_view_seniors.html",{"data":data})


def python_view_seniors(request):
    data=Employee.objects.filter(department="python",designation="senior")
    return render(request,"python_view_seniors.html",{"data":data})
