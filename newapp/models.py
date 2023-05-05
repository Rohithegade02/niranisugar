
from django.db import models
import datetime



class employee(models.Model):
    employee_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    employee_DOB = models.DateField()
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    DOJ = models.DateField()
    gender = models.CharField(max_length=20)
    salary = models.CharField(max_length=20)
    def __str__(self):
        return self.employee_name


class department(models.Model):
    Employee_name = models.ForeignKey(employee, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=200)

    def __str__(self):
        return self.department_name


class shift(models.Model):
    shift_name = models.CharField(max_length=20)
    shift_code = models.CharField(max_length=20)
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()
    grace_time = models.CharField(max_length=10)
    total_hours = models.CharField(max_length=20)

    def __str__(self):
        return self.shift_name


class attendance(models.Model):
    Employee_Name = models.ForeignKey(employee, on_delete=models.CASCADE)
    shift_of_employee = models.ForeignKey(shift, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    check_in_time = datetime.datetime.now()
    check_out_time = datetime.datetime.now()
    # def __str__(self):
    #     return self.date

class employee_shift(models.Model):
    employee_name_shift = models.ForeignKey(employee, on_delete=models.CASCADE)
    shift_allocated = models.ForeignKey(shift, on_delete=models.CASCADE)
    from_date = models.DateField()
    # def __str__(self):
    #     return self.from_date


class leavetype(models.Model):
    leave_type_name = models.CharField(max_length=200)
    approval_status = models.BooleanField(default=False)
    no_of_days_allowed = models.IntegerField()
    def __str__(self):
        return self.leave_type_name

class leave_application(models.Model):
    lemployee_ID = models.ForeignKey(employee, on_delete=models.CASCADE)
    leave_type_id = models.ForeignKey(leavetype, on_delete=models.CASCADE)
    date_of_application = models.DateField()
    l_from = models.DateField()
    l_to = models.DateField()
    no_of_days = models.IntegerField()
    reason = models.CharField(max_length=200)
    approval_status = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.reason

class account(models.Model):
    acc_employee_id = models.ForeignKey(employee, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=200)
    IFSC = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)
    account_type = models.CharField(max_length=200)

    def __str__(self):
        return self.account_type
