from django.shortcuts import render, HttpResponse
from .models import Employee, Department, Role

# Create your views here.
def index(request):
    return render(request, 'index.html' )

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    print(context)
    return render(request, 'all_emp.html', context)

def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        role = request.POST['role']
        phone = request.POST['phone']
        joining_date = request.POST['joining_date']
        new_emp = Employee(first_name=first_name, last_name=last_name, dept_id=dept, salary=salary, bonus=bonus,
                role_id=role, phone=phone, joining_date=joining_date)
        new_emp.save()
        return HttpResponse('Employee Added Successfully')
    elif request.method=='GET':
        return render(request, 'add_emp.html' )
    else:
        return HttpResponse('An Exception has been occurred')

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('Employee Removed Successfully')
        except:
            return HttpResponse('Please Enter a valid Employee ID')
    emp = Employee.objects.all()
    context = {
        'emps' : emp
    }
    return render(request, 'remove_emp.html', context)

def filter_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if first_name:
            emps = emps.filter(first_name = first_name)
        if last_name:
            emps = emps.filter(last_name = last_name)
        if dept:
            emps = emps.filter(dept__name = dept)
        if role :
            emps = emps.filter(role__name =  role)

        context = {
            'emps' : emps
        }
        return render(request, 'all_emp.html', context)
    
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    
    else:
        return HttpResponse('An Exception has been occurred')