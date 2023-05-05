from django.shortcuts import render,redirect
from .models import leave_application, leavetype, employee, shift, employee_shift
from django.http import HttpResponse


def main(request):
    return render(request, 'main.html')


def manager(request):
    return render(request, 'manager.html')



def logout(request):
    return render(request, 'logout.html')


def profile(request):
    return render(request, 'profile.html')

def emp(request):
    return render(request, 'emp.html')

def home(request):
    return render(request, 'home.html')

def viewapp(request):
    applications = leave_application.objects.all()
    return render(request, 'application.html', {'applications': applications})

def viewemp(request):
    employees = employee.objects.all()
    return render(request, 'viewemployees.html', {'employees': employees})

def viewempshift(request):
    shifts = employee_shift.objects.all()
    return render(request, 'shifts.html', {'shifts': shifts})


def shiftpolicy(request):
    shifts = shift.objects.all()
    return render(request, 'shiftpolicy.html', {'shifts': shifts})





def addemployee(request):
    if request.method == 'POST':
        employee_name = request.POST['employee_name']
        designation = request.POST['designation']
        employee_DOB = request.POST['employee_DOB']
        phone = request.POST['phone']
        email = request.POST['email']
        DOJ = request.POST['DOJ']
        gender = request.POST['gender']
        salary = request.POST['salary']
        employee.objects.create(employee_name=employee_name, designation=designation, employee_DOB=employee_DOB, phone=phone, email=email, DOJ=DOJ, gender=gender, salary=salary)
        return render(
            request,
            'addemployee.html',
            {
                'employees': employee.objects.all(),
                'msg': 'Employee Added'
            }
        )
    else:
        return render(request, 'addemployee.html', {'employees': employee.objects.all()})





def addleaveapp(request):
    if request.method == 'POST':
        lemployee_ID = int(request.POST['lemployee_ID'])
        leave_type_id_id = request.POST.get('leavetype')
        leave_type_id = leavetype.objects.get(id=leave_type_id_id)
        date_of_application = request.POST['date_of_application']
        l_from = request.POST['l_from']
        l_to = request.POST['l_to']
        no_of_days = int(request.POST['no_of_days'])
        reason = request.POST['reason']
        leave_application.objects.create(lemployee_ID_id=lemployee_ID, leave_type_id=leave_type_id, date_of_application=date_of_application, no_of_days=no_of_days, l_from=l_from, l_to=l_to, reason=reason)
        return render(
            request,
            'addleaveapp.html',
            {
                'leavetypes': leavetype.objects.all(),
                'msg': 'Leave application Added'
             }
        )
    else:
        return render(request, 'addleaveapp.html', {'leavetypes': leavetype.objects.all()})


def addempshift(request):
    if request.method == 'POST':
        employee_name_shift_id = request.POST.get('employee')
        employee_name_shift = leavetype.objects.get(id=employee_name_shift_id)
        shift_allocated_id = request.POST.get('shift')
        shift_allocated = leavetype.objects.get(id=shift_allocated_id)
        from_date = request.POST['from_date']

        employee_shift.objects.create(employee_name_shift=employee_name_shift, shift_allocated=shift_allocated, from_date=from_date)
        return render(
            request,
            'addempshift.html',
            {
                'employees': employee.objects.all(),
                'shifts': shift.objects.all(),
            }
        )
    else:
        return render(request, 'addempshift.html', {'employees': employee.objects.all(),'shifts': shift.objects.all()})



def update_true_model(request, model_id):
    mymodel = leave_application.objects.get(id=model_id)
    mymodel.approval_status=True
    mymodel.save()
    print(mymodel.approval_status)
    return render(request,'main.html')

def update_false_model(request, model_id):
    mymodel = leave_application.objects.get(id=model_id)
    mymodel.approval_status=False
    mymodel.save()
    print(mymodel.approval_status)
    return render(request,'main.html')